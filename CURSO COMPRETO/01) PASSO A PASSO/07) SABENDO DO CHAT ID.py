from TOKEN import *
import telebot
import threading

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "OLÁ USUÁRIO! MUITO OBRIGADO POR ENTRAR EM CONTATO!")
    print(message.chat.id)
  
def receber_messagem():
    bot.infinity_polling() 

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    hilo_bot = threading.Thread(name="hilo_bot", target=receber_messagem)
    hilo_bot.start()
    print("FIM")
    print("BOT REINICIADO")
    bot.send_message(ID, "IAÍ ESTUDANTE!")
