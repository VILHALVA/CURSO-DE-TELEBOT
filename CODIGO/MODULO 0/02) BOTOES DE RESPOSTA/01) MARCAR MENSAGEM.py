from TOKEN import *
import telebot
from telebot.types import ForceReply

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    marcar = ForceReply()
    bot.reply_to(message, "OLÁ USUÁRIO! MUITO OBRIGADO POR ENTRAR EM CONTATO!", reply_markup=marcar)
    
if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
