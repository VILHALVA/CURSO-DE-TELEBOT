from TOKEN import *
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "OLÁ USUÁRIO! MUITO OBRIGADO POR ENTRAR EM CONTATO!")

@bot.message_handler(commands=["video"])
def cmd_video(message):
    bot.send_chat_action(message.chat.id, "upload_video")
    video = open("./MIDIAS/sol.mp4", "rb")
    bot.send_video(message.chat.id, video, caption="VEJA O VIDEO SOBRE O SOL E A LUA!")
        
@bot.message_handler(content_types=["text"])
def bot_messagem_texto(message):  
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "COMANDO NÃO DISPONIVEL, TENTE: /start, /ayuda, /help")
    else:
         bot.send_chat_action(message.chat.id, "typing")
         bot.send_message(message.chat.id, "<b>OLÁ CARA!</b>")
        
if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
