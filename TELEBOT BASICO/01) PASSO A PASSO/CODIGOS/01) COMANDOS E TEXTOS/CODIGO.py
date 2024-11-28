from TOKEN import *
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "OLÁ USUÁRIO! MUITO OBRIGADO POR ENTRAR EM CONTATO!")
    
@bot.message_handler(content_types=["text"])
def bot_messagem_texto(message): 
    texto_html = '<b><u>FORMATOS HTML</u>:</b>' + '\n'  
    texto_html += '<b>NEGRITA</b>' + '\n'
    texto_html += '<i>CURSIVA</i>' + '\n'
    texto_html += '<u>SUBRINHADO</u>' + '\n'
    texto_html += '<s>TACHADO</s>' + '\n'
    texto_html += '<code>MONOESPACADO</code>' + '\n'
    texto_html += '*SPOILER*' + '\n'  # Usar * para negrito para criar o efeito de spoiler
    texto_html += '<a href="https://fikidelton.com/">ENLACE</a>' + '\n'
    
    texto_markdown = '*__FORMATOS MARKDOWN__*:' + '\n'
    texto_markdown += '*NEGRITO*' + '\n'
    texto_markdown += '_ITÁLICO_' + '\n'
    texto_markdown += '__SUBLINHADO__' + '\n'
    texto_markdown += '~~TACHADO~~' + '\n'
    texto_markdown += '`MONOESPACADO`' + '\n'
    texto_markdown += '**SPOILER**' + '\n'
    texto_markdown += '[ENLACE](https://fikidelton.com/)' + '\n'
       
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "COMANDO NÃO DISPONIVEL, TENTE: /start, /ayuda, /help")
    else:
        bot.send_message(message.chat.id, texto_html, parse_mode="html", disable_web_page_preview=True)
        bot.send_message(message.chat.id, texto_markdown, parse_mode="MarkdownV2", disable_web_page_preview=True)
        
if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
