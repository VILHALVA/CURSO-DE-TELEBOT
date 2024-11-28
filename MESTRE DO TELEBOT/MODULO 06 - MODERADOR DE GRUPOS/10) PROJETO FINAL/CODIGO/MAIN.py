import telebot
from DB_CONNECTION import db_connection
from TOKEN import TOKEN
from telebot import types
import re

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
        
        # Criar painel com botões
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🔨", callback_data="ban"),
                   types.InlineKeyboardButton("🤐", callback_data="mute"),
                   types.InlineKeyboardButton("🥾", callback_data="kick"),
                   types.InlineKeyboardButton("📴", callback_data="off"))

        # Enviar mensagem com o status atual e o painel de botões
        bot.send_message(message.chat.id, f"Status atual: {punishment}\nSelecione a punição:", reply_markup=markup)
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

        # Aplicar punição ao membro
        apply_punishment(call.message, punishment)
    
        # Enviar uma nova mensagem com o novo status
        new_text = f"👑STATUS ATUAL: {punishment}\n👨‍🔧CONFIGURE A PUNIÇÃO:"
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
        cursor.execute("INSERT INTO group_punishments (group_id, punishment) VALUES (%s, %s) ON DUPLICATE KEY UPDATE punishment=%s", (group_id, punishment, punishment))
        db_connection.commit()
    except Exception as e:
        print("Erro ao salvar punição:", e)
        db_connection.rollback()

def get_punishment(group_id):
    try:
        cursor.execute("SELECT punishment FROM group_punishments WHERE group_id = %s", (group_id,))
        punishment = cursor.fetchone()
        if punishment:
            return punishment[0]
        else:
            return "off"  # Padrão para desligar o anti-spam se nenhuma punição estiver configurada
    except Exception as e:
        print("Erro ao obter punição:", e)

# Função para aplicar punição ao membro
def apply_punishment(message, punishment):
    try:
        # Exclui a mensagem do membro punido
        bot.delete_message(message.chat.id, message.message_id)
    except:
        pass

    if message.from_user.id != bot.get_me().id:  # Verifica se o usuário punido não é o próprio bot
        if punishment == "ban":
            # Aplicar banimento
            bot.kick_chat_member(message.chat.id, message.from_user.id)
        elif punishment == "mute":
            # Aplicar silenciamento
            bot.restrict_chat_member(message.chat.id, message.from_user.id, types.ChatPermissions())
        elif punishment == "kick":
            # Aplicar kick
            bot.kick_chat_member(message.chat.id, message.from_user.id)
        elif punishment == "off":
            # Desligar anti-spam
            pass # Coloque o código relevante aqui, se necessário

# Handler para mensagens de texto
@bot.message_handler(func=lambda message: True)
def anti_spam(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = message.text

    # Verifica se o remetente não é um bot
    if not message.from_user.is_bot:
        # Verifica se o remetente é um administrador do grupo
        member = bot.get_chat_member(chat_id, user_id)
        if not member.status in ["creator", "administrator"]:
            # Verifica se a mensagem contém algum tipo de link
            if re.search(r'http[s]?://[^\s<>"]+|www\.[^\s<>"]+', text):
                # Remove a mensagem do usuário
                bot.delete_message(chat_id, message.message_id)
                # Aplica a punição conforme configurado no MySQL
                punishment = get_punishment(chat_id)
                apply_punishment(message, punishment)
                # Envie uma mensagem de aviso ao grupo (você pode personalizar essa mensagem)
                bot.send_message(chat_id, f"Usuário {message.from_user.first_name} foi punido por enviar spam!")

if __name__ == '__main__':
    print("Bot Iniciado!")
    bot.polling()
