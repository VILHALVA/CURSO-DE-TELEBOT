from TOKEN import *
import telebot
import threading

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "OLÁ USUÁRIO! MUITO OBRIGADO POR ENTRAR EM CONTATO!")
    print(message.chat.id)
        
@bot.message_handler(content_types=["text"])
def bot_messagem_texto(message):  
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "COMANDO NÃO DISPONIVEL, TENTE: /start, /ayuda, /help")
    else:
         bot.send_chat_action(message.chat.id, "typing")
         bot.send_message(message.chat.id, "<b>EU FUI INICIALIZADO POR ALGUM MOTIVO!</b>")
  
def receber_messagem():
    bot.infinity_polling() 

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    hilo_bot = threading.Thread(name="hilo_bot", target=receber_messagem)
    hilo_bot.start()
    print("FIM")
    print("BOT REINICIADO")
    bot.send_message(CANAL, "MUITO OBRIGADO POR ME TORNAR ADM DO SEU CANAL. CASO VOCÊ NÃO SAIBA COMO ENCONTRAR O ID DO SEU CANAL, CLIQUE AQUI: https://t.me/CODIGOCN/1431!")
