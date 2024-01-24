import telebot
from imagekitio import ImageKit
from base64 import b64encode
 
TOKEN = "TOKEN_DO_BOT"
IK_PUBLIC = 'IK_PUBLIC'
IK_PRIVATE = 'IK_PRIVATE'
IK_URL = 'URL-DA_IMAGEM'
ik = ImageKit(public_key=IK_PUBLIC, private_key=IK_PRIVATE, url_endpoint=IK_URL)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.send_message(m.chat.id, "<b>OLÁ USUÁRIO BEM VINDO!</b>\nDIGITE /foto para receber uma foto com descrição enorme!", parse_mode="html")
    
def ik_subir_imagem(ruta_imagem):
    with open(ruta_imagem, "rb") as f:
        imagem = b64encode(f.read())
    print("SUBINDO A IMAGEM!")
    try:
        res = ik.upload_file(file=imagem, file_name="imagem.jpg")
    except Exception as e:
        return f"ERROR: {e.messsage}"
    status_code = res.response_metadata.http_status_code
    if status_code == 200:
        return res.response_metadata.raw
    else:
        return f"ERROR: {status_code}"
    
def enviar_foto(cid, foto, texto=""):
    print(f"A MENSAGEM TEM {len(texto)} CARACTERES!")
    if len(texto) <= 1024:
        bot.send_photo(cid, open(foto, "rb"), caption=texto, parse_mode="html")
    else:
        url_foto = ik_subir_imagem(foto).get("url")
        mensagem = f'<a href={url_foto}"> </a>\n{texto}'
        if len(mensagem) <= 4096:
            bot.send_message(cid, mensagem, parse_mode="html")
        else:
            print(f"ERROR: A MENSAGEM TEM {len(mensagem)} CARACTERES!")
    
@bot.message_handler(commands=['foto'])
def cmd_foto(m):
    cid = m.chat.id
    texto1 = "<b>PROVA DE MENSAGEM LONGA</b>"
    texto2 = "X"*1024
    enviar_foto(cid, "./imagem/foto.jpg", texto2)
    
if __name__ == '__main__':
    print("BOT INICIADO!")
    bot.infinity_polling(timeout=60)