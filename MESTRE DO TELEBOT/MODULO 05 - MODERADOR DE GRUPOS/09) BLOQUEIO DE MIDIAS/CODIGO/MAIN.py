import telebot
from DB_CONNECTION import db_connection
from TOKEN import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)

# Conexão com o banco de dados MySQL
connection = db_connection
cursor = connection.cursor()

# Handler para comandos /settings
@bot.message_handler(commands=['settings'])
def handle_settings(message):
    # Verificar se o usuário é um administrador do grupo
    if message.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(message.chat.id)]:
        
        # Buscar a punição atual do grupo no MySQL
        group_id = message.chat.id
        punishment = get_punishment(group_id)
        
        # Criar painel com botões para bloquear mídias
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("📸 Foto", callback_data="photo"),
                   types.InlineKeyboardButton("🎞 Vídeo", callback_data="video"),
                   types.InlineKeyboardButton("🎥 Gif", callback_data="gif"),
                   types.InlineKeyboardButton("🎧 Áudio", callback_data="audio"))

        # Enviar mensagem com o status atual e o painel de botões
        bot.send_message(message.chat.id, f"Status atual: {punishment}\nSelecione a mídia para bloquear:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Você não é um administrador deste grupo.")

# Handler para callback query dos botões
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    # Verificar se o usuário é um administrador do grupo
    if call.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(call.message.chat.id)]:
        punishment = call.data
        group_id = call.message.chat.id

        # Salvar a punição no banco de dados
        save_punishment(group_id, punishment)

        # Enviar uma nova mensagem com o novo status
        new_text = f"👑STATUS ATUAL: {punishment}\n👨‍🔧CONFIGURE O BLOQUEIO DE MÍDIA:"
        try:
            sent_message = bot.send_message(chat_id=call.message.chat.id, text=new_text, reply_markup=call.message.reply_markup)
            
            # Excluir a mensagem anterior
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except:
            pass
    else:
        bot.answer_callback_query(call.id, "Você não é um administrador deste grupo.")

# Funções para salvar e obter a punição do banco de dados
def save_punishment(group_id, punishment):
    try:
        cursor.execute("INSERT INTO group_punishments (group_id, photo, video, gif, audio) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE photo=%s, video=%s, gif=%s, audio=%s", (group_id, "on" if punishment == "photo" else "off", "on" if punishment == "video" else "off", "on" if punishment == "gif" else "off", "on" if punishment == "audio" else "off", "on" if punishment == "photo" else "off", "on" if punishment == "video" else "off", "on" if punishment == "gif" else "off", "on" if punishment == "audio" else "off"))
        db_connection.commit()
    except Exception as e:
        print("Erro ao salvar punição:", e)
        db_connection.rollback()

def get_punishment(group_id):
    try:
        cursor.execute("SELECT photo, video, gif, audio FROM group_punishments WHERE group_id = %s", (group_id,))
        punishment = cursor.fetchone()
        if punishment:
            photo, video, gif, audio = punishment
            if photo == "on":
                return "photo"
            elif video == "on":
                return "video"
            elif gif == "on":
                return "gif"
            elif audio == "on":
                return "audio"
            else:
                return "off"
        else:
            return "off"  # Padrão para desligar o bloqueio de mídia se nenhuma punição estiver configurada
    except Exception as e:
        print("Erro ao obter punição:", e)

# Handler para mensagens de mídia
@bot.message_handler(content_types=['photo', 'video', 'document', 'audio'])
def handle_media(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    content_type = message.content_type

    # Verifica se o remetente não é um bot
    if not message.from_user.is_bot:
        # Verifica se o remetente é um administrador do grupo
        member = bot.get_chat_member(chat_id, user_id)
        if not member.status in ["creator", "administrator"]:
            # Bloqueia a mídia
            punishment = get_punishment(chat_id)
            apply_punishment(message, punishment)

# Função para aplicar punição de mídia
def apply_punishment(message, punishment):
    try:
        # Aplica a punição adequada conforme configurado
        if punishment == "photo":
            # Bloqueia o envio de fotos
            bot.delete_message(message.chat.id, message.message_id)
        elif punishment == "video":
            # Bloqueia o envio de vídeos
            bot.delete_message(message.chat.id, message.message_id)
        elif punishment == "gif":
            # Bloqueia o envio de gifs
            bot.delete_message(message.chat.id, message.message_id)
        elif punishment == "audio":
            # Bloqueia o envio de áudios
            bot.delete_message(message.chat.id, message.message_id)
        elif punishment == "off":
            # Não faz nada se estiver desativado
            pass
    except Exception as e:
        print("Erro ao aplicar punição:", e)

if __name__ == '__main__':
    print("Bot Iniciado!")
    bot.polling()
