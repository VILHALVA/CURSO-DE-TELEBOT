import telebot
TOKEN = "TOKEN AQUI"
bot = telebot.TeleBot(TOKEN)

chat_id = "ID DO CHAT AQUI"

bot.send_photo(chat_id, open("NOME DA MIDIA AQUI", "rb"))

