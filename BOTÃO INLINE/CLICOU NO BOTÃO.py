from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler

# Configuração do bot
bot_token = 'seu_token_aqui'
updater = Updater(bot_token, use_context=True)

# Função para lidar com a consulta do botão
def button_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Você clicou no botão!")

# Função para enviar a mensagem com o botão inline
def send_inline_button(update, context):
    keyboard = [[InlineKeyboardButton("Clique aqui", callback_data='button_clicked')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Clique no botão abaixo:', reply_markup=reply_markup)

# Registro dos handlers
updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
updater.dispatcher.add_handler(CommandHandler('start', send_inline_button))

# Inicialização do bot
updater.start_polling()
updater.idle()

# Para criar um bot do Telegram em Python que envia uma mensagem quando um usuário clica em um botão inline, podemos utilizar a biblioteca python-telegram-bot.

# Antes de começar, é necessário criar um bot e obter o seu token de acesso. Em seguida, vamos utilizar a classe InlineKeyboardButton para criar um botão inline e a classe InlineKeyboardMarkup para colocar esse botão em uma mensagem. Quando o usuário clicar no botão, o Telegram enviará uma consulta para o nosso bot, que deve responder com a mensagem desejada.

# No código acima, a função send_inline_button cria um botão inline com o texto "Clique aqui" e o callback data "button_clicked". Em seguida, essa função envia uma mensagem para o usuário com o botão inline usando a função update.message.reply_text.

# A função button_handler é registrada como um handler para consultas de botão inline usando a classe CallbackQueryHandler. Quando o usuário clica no botão, o Telegram envia uma consulta para o nosso bot contendo o callback data do botão. A função button_handler é executada para lidar com essa consulta, enviando uma mensagem com o texto "Você clicou no botão!" usando a função query.edit_message_text.

# Por fim, registramos os handlers e iniciamos o bot usando as funções add_handler, start_polling e idle.

# Com esse código, o usuário pode clicar no botão inline para receber a mensagem "Você clicou no botão!" do nosso bot.