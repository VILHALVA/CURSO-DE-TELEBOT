import telebot
import subprocess

TOKEN = "TOKEN_AQUI" # Substitua pelo Token do seu bot
ADMINS = "ID_AQUI"  # Substitua pelo seu ID de administrador
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.send_message(m.chat.id, "<b>OLÁ USUÁRIO BEM VINDO!</b>\n<code>DIGITE /c MAIS O COMANDO DO CMD</code>", parse_mode="html")
    
def es_admin(cid, info=True):
    if cid == ADMINS:
        return True
    else:
        if info:
            print(f"{cid} NÃO ESTÁ AUTORIZADO!")
            bot.send_message(cid, f"❌<b>{cid} NÃO ESTÁ AUTORIZADO!</b>", parse_mode="html")
        return False
    
@bot.message_handler(commands=['c'])
def cmd_c(m):
    if es_admin(m.chat.id):
        param = m.text.split()
        if len(param) == 1:
            bot.send_message(m.chat.id, "🔴NÃO FOI INDICADO NENHUM COMANDO!")
        else:
            comando = " ".join(param[1:])
            r = subprocess.run(
            comando,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,  
            universal_newlines=True
        )

            texto = ""
            if r.returncode:
                texto += f"ERRO: {r.returncode}\n"
            else:
                if not r.stdout and not r.stderr:
                    texto += "✅COMANDOS FORAM EXECUTADOS COM SUCESSO!\n"
            if r.stdout:
                texto += r.stdout
            if r.stderr:
                texto += r.stderr
            bot.send_message(m.chat.id, texto)
    
if __name__ == '__main__':
    print("BOT INICIADO!")
    bot.infinity_polling(timeout=60)