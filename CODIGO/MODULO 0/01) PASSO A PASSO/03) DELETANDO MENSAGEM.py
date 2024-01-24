from TOKEN import *
import telebot
from time import sleep

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "OLÁ USUÁRIO! MUITO OBRIGADO POR ENTRAR EM CONTATO!")
    
@bot.message_handler(content_types=["text"])
def bot_messagem_texto(message):  
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "COMANDO NÃO DISPONIVEL, TENTE: /start, /ayuda, /help")
    else:
        # x = bot.send_message(message.chat.id, "<b>OLÁ CARA!</b>", parse_mode="html", disable_web_page_preview=True)
        # sleep(3)
        # bot.delete_message(message.chat.id, x.message_id)
        sleep(3)
        bot.delete_message(message.chat.id, message.message_id)
        
if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
