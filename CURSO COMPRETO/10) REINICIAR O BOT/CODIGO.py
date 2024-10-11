import telebot
import sys
import platform
import os

TOKEN = "TOKEN_AQUI" # Substitua pelo Token do seu bot
ADMINS = "ID_AQUI"  # Substitua pelo seu ID de administrador
bot = telebot.TeleBot(TOKEN)

def es_admin(cid, info=True):
    if cid == ADMINS:
        return True
    else:
        if info:
            print(f"{cid} NÃO ESTÁ AUTORIZADO!")
            bot.send_message(cid, f"<b>{cid} NÃO ESTÁ AUTORIZADO!</b>", parse_mode="html")
        return False
    
@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.send_message(m.chat.id, "Olá Seja bem-vindo!\nENVIE /restart se quiser me reiniciar!")
    
@bot.message_handler(commands=['restart'])
def cmd_restart(m):
    if es_admin(m.chat.id):
        print("BOT REINICIADO!")
        bot.send_message(m.chat.id, "<b>🔁BOT REINICIADO!</b>", parse_mode="html")
        bot.stop_polling()
        os.execv(sys.executable, sys.argv)
        
@bot.message_handler(commands=['reboot'])
def cmd_reboot(m):
    if es_admin(m.chat.id):
        print("SERVIDOR REINICIADO!")
        bot.send_message(m.chat.id, "<b>🔁SERVIDOR REINICIADO!</b>", parse_mode="html")
        if platform.system() == "Windows":
            os.system("shutdown /r") 
        elif platform.system() == "Linux":
            os.system("reboot") 
            
if __name__ == '__main__':
    print("BOT INICIADO!")
    bot.infinity_polling(timeout=60)