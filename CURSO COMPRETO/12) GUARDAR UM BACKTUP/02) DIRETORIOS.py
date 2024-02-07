import telebot
import zipfile
import tempfile
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

def zipdir(nome_arquivo, diretorio='.', excluir=[]):
    ruta_zip = f'{tempfile.gettempdir()}/{nome_arquivo}'    
    with zipfile.ZipFile(ruta_zip, "w", zipfile.ZIP_DEFLATED) as f:
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                ruta = os.path.join(root, file)
                comprimir = True
                for ex in excluir:
                    if ex in ruta or ex.replace('/','\\') in ruta:
                        print(f"OMITINDO: {ruta}")
                        comprimir = False
                        break
                    if comprimir:
                        print(f"COMPRIMINDO: {ruta}")
                        f.write(ruta)
    return ruta_zip
    
@bot.message_handler(commands=['backtup'])
def cmd_backtup(m):
    cid = m.chat.id  
    if es_admin(cid): 
        excluir = ('/__pycache__/', 'musica.mp3')
        ruta_zip = zipdir("mi_bot.zip", ".", excluir)
        bot.send_document(cid, open(ruta_zip, 'rb'), parse_mode='html')
        os.remove(ruta_zip)
   
if __name__ == '__main__':
    print("BOT INICIADO!")
    bot.infinity_polling(timeout=60)