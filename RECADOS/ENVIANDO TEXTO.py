import telebot
TOKEN = "TOKEN AQUI"
bot = telebot.TeleBot(TOKEN)

chat_id = "ID DO CHAT AQUI"

bot.send_message(chat_id, '''TEXTO AQUI''')

