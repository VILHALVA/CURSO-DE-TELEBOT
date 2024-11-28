import telebot
from frikiapps.colores import *
from frikiapps.chat_gpt import ChatGpt

OPEN_AI = "TOKEN_AI"
OPEN_PASS = "SENHA_AI"
TOKEN = "TOKEN_DO_BOT"
bot = telebot.TeleBot(TOKEN)

chatgpt = ChatGpt(OPEN_AI, OPEN_PASS, headless=False)

@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.send_message(m.chat.id, "<b>OLÁ USUÁRIO BEM VINDO!</b>\nEU SOU CLIENTE DO CHATGPT!", parse_mode="html")
    
@bot.message_handler(content_types=['text'])
def mensagens_recebidas(m):
    resposta = chatgpt.chatear(m.text, formato="html")
    bot.send_message(m.chat.id, resposta, parse_mode="html", disable_web_page_preview=True)
    
if __name__ == '__main__':
    print("BOT INICIADO!")
    print(f"{verde}BOT INICIADO{gris}")
    bot.infinity_polling(timeout=60)
