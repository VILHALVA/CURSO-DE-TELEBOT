import telebot
import time
import os

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

CARPETA = "modo_lento"

if not os.path.isdir(CARPETA):
    os.mkdir(CARPETA)
    
MODO_LENTO = 10

@bot.message_handler(commands=['start'])
def cmd_start(m):
    texto = '<b>BOT INICIADO...</b>'
    bot.send_message(m.chat.id, texto, parse_mode='html')
    
def esperar(cid):
    def guardar(cid):
        with open(f'{CARPETA}/{cid}', "w", encoding='utf-8') as f:
            f.write(f'{int(time.time())}')
    if not os.path.isfile(f'{CARPETA}/{cid}'):
        guardar(cid)
        return False
    with open(f'{CARPETA}/{cid}', "r", encoding='utf-8') as f:
        timestamp = int(f.read())
    segundos = int(time.time()) - timestamp
    if segundos >= MODO_LENTO:
        guardar(cid)
        return False
    else:
        mensagem = f"VOCÊ DEVE ESPERAR <code>{MODO_LENTO-segundos}</code> SEGUNDOS!"
        bot.send_message(cid, mensagem, parse_mode='html')
        return True
    
@bot.message_handler(func=lambda x: True)
def mensagens_recebidas(m):
    if esperar(m.chat.id):
        bot.delete_message(m.chat.id, m.message_id)
        return
    bot.send_message(m.chat.id, "<b>PROCESSANDO...</b>", parse_mode="html")
    
if __name__ == '__main__':
    bot.infinity_polling(timeout=60)
        
    

