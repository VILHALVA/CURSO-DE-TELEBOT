import telebot
TOKEN_BOT = "TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN_BOT)

@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.send_message(m.chat.id, "OLÁ USUÁRIO!")
    
@bot.message_handler(content_types=['text'])
def cmd_resposta(m):
    bot.send_message(m.chat.id, m.text, parse_mode='html')
    
if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()