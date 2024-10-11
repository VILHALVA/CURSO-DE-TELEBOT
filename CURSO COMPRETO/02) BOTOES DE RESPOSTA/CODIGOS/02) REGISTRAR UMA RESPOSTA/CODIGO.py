from TOKEN import *
import telebot
from telebot.types import ForceReply

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    marcar = ForceReply()
    user_nome = bot.reply_to(message, "QUAL É O SEU NOME?", reply_markup=marcar)
    bot.register_next_step_handler(user_nome, perguntar_nome)
  
def perguntar_nome(message):
    nome = message.text
    print(f"SEU NOME É {nome}!")
    
if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
