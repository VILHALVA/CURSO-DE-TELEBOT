# MAIN.py
import telebot
import ASTRONOMIA
import CIENCIA
import TECNOLOGIA
import TELEGRAM

TOKEN = "SEU_TOKEN"
bot = telebot.TeleBot(TOKEN)

# Handler para o comando /start ou /menu
@bot.message_handler(commands=["start", "menu"])
def menu_principal(message):
    markup = telebot.types.InlineKeyboardMarkup()
    
    astronomia_button = telebot.types.InlineKeyboardButton("ASTRONOMIA", callback_data='astronomia')
    
    ciencia_button = telebot.types.InlineKeyboardButton("CIÊNCIA", callback_data='ciencia')
    
    tecnologia_button = telebot.types.InlineKeyboardButton("TECNOLOGIA", callback_data='tecnologia')
    
    telegram_button = telebot.types.InlineKeyboardButton("TELEGRAM", callback_data='telegram')
    
    markup.add(astronomia_button, ciencia_button, tecnologia_button, telegram_button)
    
    texto = '''
🛑ESCOLHA UMA DAS OPÇÕES:
'''
    bot.send_message(message.chat.id, texto, reply_markup=markup)

# Handler para os callbacks dos botões
@bot.callback_query_handler(func=lambda call: True)
def callback_query_handler(call):
    if call.data == 'astronomia':
        bot.send_message(call.message.chat.id, "😙SELECIONE UMA OPÇÃO DE ASTRONOMIA!\n👉CLIQUE EM /start PARA VOLTAR!", reply_markup=ASTRONOMIA.submenu_astronomia())
    elif call.data == 'ciencia':
        bot.send_message(call.message.chat.id, "😙SELECIONE UMA OPÇÃO DE CIÊNCIA!\n👉CLIQUE EM /start PARA VOLTAR!", reply_markup=CIENCIA.submenu_ciencia())
    elif call.data == 'tecnologia':
        bot.send_message(call.message.chat.id, "😙SELECIONE UMA OPÇÃO DE TECNOLOGIA!\n👉CLIQUE EM /start PARA VOLTAR!", reply_markup=TECNOLOGIA.submenu_tecnologia())
    elif call.data == 'telegram':
        bot.send_message(call.message.chat.id, "😙SELECIONE UMA OPÇÃO DE TELEGRAM!\n👉CLIQUE EM /start PARA VOLTAR!", reply_markup=TELEGRAM.submenu_telegram())
    else:
        ASTRONOMIA.callback_query(bot, call)
        CIENCIA.callback_query(bot,call)
        TECNOLOGIA.callback_query(bot, call)
        TELEGRAM.callback_query(bot, call)

# Iniciar o bot
bot.polling()
