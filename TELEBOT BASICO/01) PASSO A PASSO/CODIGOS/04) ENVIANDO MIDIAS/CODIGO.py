from TOKEN import *
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "OLÁ USUÁRIO! MUITO OBRIGADO POR ENTRAR EM CONTATO!")
    
@bot.message_handler(commands=["foto", "imagem"])
def cmd_foto(message):
    foto = open("./MIDIAS/telegram.jpg", "rb")
    bot.send_photo(message.chat.id, foto, "1O ANOS DE TELEGRAM")
    
@bot.message_handler(commands=["video"])
def cmd_video(message):
    video = open("./MIDIAS/sol.mp4", "rb")
    bot.send_video(message.chat.id, video, caption="VEJA O VIDEO SOBRE O SOL E A LUA!")
    
@bot.message_handler(commands=["pdf", "livro"])
def cmd_pdf(message):
    pdf = open("./MIDIAS/Python.pdf", "rb")
    bot.send_document(message.chat.id, pdf, caption="ESTUDE PYTHON DE VERDADE: https://pt.wikipedia.org/wiki/Python!")
    
@bot.message_handler(content_types=["text"])
def bot_messagem_texto(message):  
    if message.text and message.text.startswith("/"):
        bot.send_message(message.chat.id, "COMANDO NÃO DISPONIVEL, TENTE: /start, /ayuda, /help /foto /livro")
    else:      
        bot.send_message(message.chat.id, "EU SÓ RESPONDO A COMANDOS!") 
        
if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
