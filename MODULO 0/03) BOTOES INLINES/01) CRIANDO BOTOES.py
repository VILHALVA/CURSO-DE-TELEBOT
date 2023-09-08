from TOKEN import *
import telebot
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    marca = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton("BOTÕES INLINE", url="https://youtu.be/9g7uzYv-5ys?si=a0AuWd0Hl1s8RxKi")
    b2 = InlineKeyboardButton("CRIANDO BOTS", url="https://github.com/VILHALVA/CURSO-TELEGRAM-BOT")
    b3 = InlineKeyboardButton("CURSO DE PHP", url="https://github.com/VILHALVA/CURSO-DE-PHP")
    b4 = InlineKeyboardButton("CURSO DE JAVA", url="https://github.com/VILHALVA/CURSO-DE-JAVA")
    b5 = InlineKeyboardButton("CURSO DE PYTHON", url="https://github.com/VILHALVA/CURSO-DE-PYTHON")
    
    marca.add(b1, b2, b3, b4, b5)
    bot.send_message(message.chat.id, "CLIQUE NOS BOTÕES PARA FAZER O CURSO:", reply_markup=marca)

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")