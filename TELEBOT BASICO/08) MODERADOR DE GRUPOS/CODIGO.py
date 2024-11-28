import telebot
from datetime import datetime, timedelta
import re
import os
from pprint import pprint
from shutil import move

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

D = {
    "avisos": "avisos",
    "banidos": "banidos",
    "baneados": "baneados" 
}

for clave, valor in D.items():
    if not os.path.isdir(valor):
        os.mkdir(valor)
        
MAX_AVISOS = 3
palavras_proibidas = ["bro", "cu", "literal", "puta"]

@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.send_message(m.chat.id, "OLÁ USUÁRIO! EU SOU MODERADOR DE GRUPOS!")
    
@bot.message_handler(content_types=["new_chat_members"])
def boas_vindas(m):
    for x in m.new_chat_members:
        bot.send_message(m.chat.id, f"<b>SEJA BEM VINDO AO GRUPO, {x.first_name}!</b>", parse_mode="html")

def avisar(cid, uid, nome):
    if not os.path.isfile(f'{D["avisos"]}/{cid}_{uid}'):
        avisos = 1
    else:
        with open(f'{D["avisos"]}/{cid}_{uid}', "r", encoding="utf-8") as f:
            avisos = int(f.read().split("\n")[0])
        avisos += 1
    
    texto = f"<b>AVISO</b><code>{avisos}</code> de <code>{MAX_AVISOS}</code>\n"
    texto += f"<i>{nome}</i> INFRINGIU AS REGRAS!"
    bot.send_message(cid, texto, parse_mode="html")
    
    if avisos < MAX_AVISOS:
        with open(f'{D["avisos"]}/{cid}_{uid}', "w", encoding="utf-8") as f:
            f.write(f"{avisos}\n{nome}")
    else:
        try:
            bot.ban_chat_member(cid, uid)
        except Exception as e:
            print(f"ERROR: {e}")
            return
        print(f"{nome}({uid}) FOI BANIDO DO GRUPO!")
        bot.send_message(cid, f"<b>{nome} ({uid}) FOI BANIDO DO GRUPO!</b>", parse_mode="html")
        move(f'{D["avisos"]}/{cid}_{uid}', f'{D["banidos"]}/{cid}_{uid}')
            
def palavras(texto):
    encontrado = False
    for palavra in palavras_proibidas:
        if re.search(r'\b' + palavra + r'\b', texto, flags=re.IGNORECASE):
            encontrado = True
            break
    return encontrado

@bot.message_handler(commands=['unban'])
def cmd_unban(m):  
    cid = m.chat.id
    info_membro = bot.get_chat_member(cid, m.from_user.id)
    pprint(info_membro.__dict__)
    if not info_membro.status in ["creator", "administrator"]:
        return
    archivos = os.listdir(D["baneados"])
    if not archivos:
        bot.send_message(cid, "NÃO HÁ MEMBROS BANIDOS!")
        return
    else:
        membros = []
        for arquivo in archivos:
            with open(f'{D["baneados"]}/{arquivo}', "r", encoding="utf-8") as f:
                membro = f.read().split("\n")[1]
                membros.append(membro, arquivo)
        param = m.text.split()
        if len(param) == 1:
            texto = ""
            n = 0
            for membro, arquivo in membros:
                n += 1
                texto += f"<code>{n}</code> {membro}\n"
            bot.send_message(cid, texto, parse_mode="html")
        else:
            indice = int(param[1])
            dados = membros[indice-1]
            membro = dados[1]
            icid, iuid = dados[1].split("_")
            res = bot.unban_chat_member(icid, iuid, only_if_banned=True)
            if res:
                bot.delete_message(cid, m.message_id)
                bot.send_message(cid, f"<code>O MEMBRO {membro} FOI DESBANIDO!</code>", parse_mode="html")
                os.remove(f"{D['baneados']}/{dados[1]}")
            else:
                bot.send_message(cid, f"<b>ERRO AO DESBANIR {membro}!</b>", parse_mode="html")
        
 
@bot.message_handler(func=lambda x: True)        
def mensagens_recebidas(m):
    cid = m.chat.id
    uid = m.from_user.id
    nome = m.from_user.first_name
    print(f"{nome}: {m.text}")  
    
    if palavras(m.text):
        bot.delete_message(cid, m.message_id)  
        avisar(cid, uid, nome)
            
if __name__ == '__main__':
    bot.infinity_polling(timeout=60)