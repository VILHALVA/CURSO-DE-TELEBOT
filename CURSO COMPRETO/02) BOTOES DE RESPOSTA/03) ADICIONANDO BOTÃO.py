from TOKEN import *
import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    marcar = ForceReply()
    user_idade = bot.reply_to(message, "QUAL É A SUA IDADE?", reply_markup=marcar)
    bot.register_next_step_handler(user_idade, perguntar_idade)
    
def perguntar_idade(message):
    if not message.text.isdigit():
        marcar = ForceReply()
        user_idade = bot.reply_to(message, "ERRO! DIGITE UM NÚMERO: QUAL É A SUA IDADE?", reply_markup=marcar)
        bot.register_next_step_handler(user_idade, perguntar_idade)
    else:
        marcar = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder="CLICA NO BOTÃO!")
        marcar.add("HOMEM", "MULHER")
        user_sexo = bot.reply_to(message, "QUAL É O SEU SEXO?", reply_markup=marcar)
        
if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")