import telebot
TOKEN = "TOKEN AQUI"
bot = telebot.TeleBot(TOKEN)

chat_id = "ID DO GRUPO AQUI"

#bot.send_photo(chat_id, open("TELEGRAM.webp", "rb"))
bot.send_message(chat_id, '''TEXTO''')

