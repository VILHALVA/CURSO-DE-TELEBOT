import telebot
import time
from flask import Flask, request
from pyngrok import ngrok

TOKEN_BOT = "TOKEN_AQUI" # Substitua pelo token do seu bot
TOKEN_NGROK = "TOKEN_AQUI"  # Substitua pelo seu token do Ngrok

bot = telebot.TeleBot(TOKEN_BOT)

web_server = Flask(__name__)

@web_server.route('/', methods=['POST'])
def webhook():
    if request.headers.get("content-type") == "application/json":
        update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
        bot.process_new_updates([update])
        return "OK", 200

@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.send_message(m.chat.id, "OLÁ USUÁRIO!")

@bot.message_handler(content_types=['text'])
def cmd_resposta(m):
    bot.send_message(m.chat.id, m.text, parse_mode='html')

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    ngrok_tunnel = ngrok.connect(5000)
    ngrok_url = ngrok_tunnel.public_url
    print("URL NGROK:", ngrok_url)
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=ngrok_url)
    web_server.run(host="0.0.0.0", port=5000)
