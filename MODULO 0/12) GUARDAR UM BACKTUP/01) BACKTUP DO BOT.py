import telebot
import shutil
import os

TOKEN = "TOKEN_AQUI" # Substitua pelo Token do seu bot
ADMINS = "ID_AQUI"  # Substitua pelo seu ID de administrador
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.send_message(m.chat.id, "<b>OLÁ USUÁRIO BEM VINDO!</b>\nDIGITE /backtup para fazer o backtup desse bot!", parse_mode="html")
    
def es_admin(cid, info=True):
    if cid == ADMINS:
        return True
    else:
        if info:
            print(f"{cid} NÃO ESTÁ AUTORIZADO!")
            bot.send_message(cid, f"❌<b>{cid} NÃO ESTÁ AUTORIZADO!</b>", parse_mode="html")
        return False
    
@bot.message_handler(commands=['backtup'])
def cmd_backtup(m):
    if es_admin(m.chat.id):
        script_directory = os.path.dirname(os.path.abspath(__file__))  
        backup_zip_path = os.path.join(script_directory, "..", "backtup.zip") 
        print("COMPRIMINDO OS ARQUIVOS!")
        shutil.make_archive(backup_zip_path[:-4], "zip", script_directory) 
        print("ENVIANDO O BACKTUP AO TELEGRAM...")
        bot.send_document(m.chat.id, open(backup_zip_path, "rb"), caption="BACKTUP DO BOT")
        print("ELIMINDO O BACKTUP DO DISCO!")
        os.remove(backup_zip_path)
    
if __name__ == '__main__':
    print("BOT INICIADO!")
    bot.infinity_polling(timeout=60)