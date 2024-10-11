import telebot
import time
import os

TOKEN = "TOKEN_AQUI"  

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(m):
    texto = '<b>✅BOT INICIADO!</b>'
    bot.send_message(m.chat.id, texto, parse_mode='html')

@bot.message_handler(commands=['prova']) 
def cmd_prova(m):
    cid = m.chat.id
    mid = barra(0, "INICIANDO...", cid)
    time.sleep(2)
    barra(0, "PREPARANDO...", cid, mid)
    time.sleep(1)
    barra(15, "REVISANDO...", cid, mid)
    time.sleep(3)
    barra(25, "ORDENANDO...", cid, mid)
    time.sleep(3)
    barra(52, "ALICANDO...", cid, mid)
    time.sleep(1)
    barra(76, "ESTÁ TERMINANDO...", cid, mid)
    time.sleep(2)
    barra(100, "COMPRETO!", cid, mid)
    
def cursor_arriba(n=1):
    print(f'\33[{n}A', end='')
    
def barra(porcentagem, texto="", cid=None, mid=None, terminal=True):
    t, no, si = ('█', '⬜', '⬛')
    if terminal: 
        branco = '\33[1;37m'
        amarelo = '\33[1;33m'
        verde1 = '\33[0;37m'
        verde2 = '\33[0;90m'
        ancho = os.get_terminal_size().columns -7
        cuadros_si = porcentagem * ancho // 100
        cuadros_no = ancho - cuadros_si
        barra_terminal = f'\33[K{branco}|{amarelo}{t*cuadros_si}{verde2}{t*cuadros_no}| {porcentagem:>3}%{verde1}'
        texto_terminal = f'\33[K{amarelo} {texto}\n{barra_terminal}'
        print(texto_terminal)
        if porcentagem < 100:
            cursor_arriba(2)
    
    if cid:
        cuadros_si = porcentagem // 10
        cuadros_no = 10 - cuadros_si
        barra_telegram = si*cuadros_si + no*cuadros_no
        mensagem_telegram = f'{texto}\n{barra_telegram} <code>{porcentagem:>3}%</code>'
        if not mid:
            msg = bot.send_message(cid, mensagem_telegram, parse_mode="html")
            return msg.message_id
        else:
            if porcentagem < 100:
                bot.edit_message_text(mensagem_telegram, cid, mid, parse_mode="html")
                return
            elif porcentagem == 100:
                bot.edit_message_text(mensagem_telegram, cid, mid, parse_mode="html")
                bot.delete_message(cid, mid)
                return
            else:
                bot.delete_message(cid, mid)
                return
            
if __name__ == '__main__':
    bot.infinity_polling(timeout=60)
