import logging
import pyporn
from telegram.ext import Updater, MessageHandler, Filters

# Configuração do bot
TOKEN = 'seu_token_aqui'
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Configuração do logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Função para lidar com as mensagens
def handle_message(update, context):
    # Obtém a mensagem e o chat em que ela foi enviada
    message = update.message
    chat = message.chat

    # Verifica se a mensagem contém pornografia
    if pyporn.contains_porn(message.text):
        # Remove a mensagem
        context.bot.delete_message(chat.id, message.message_id)
        # Bane o usuário
        context.bot.kick_chat_member(chat.id, message.from_user.id)

# Registra o manipulador de mensagens
dispatcher.add_handler(MessageHandler(Filters.text & Filters.group, handle_message))

# Inicia o bot
updater.start_polling()

# Para criar um bot do Telegram em Python que remove mensagens contendo conteúdo pornográfico e bane os usuários que as enviaram em um grupo, podemos usar a biblioteca python-telegram-bot.

# Antes de começar, é necessário criar um bot e obter o seu token de acesso. Em seguida, vamos criar um manipulador de mensagens para o bot que será executado sempre que uma mensagem for enviada para o grupo em que o bot está. Dentro desse manipulador, vamos verificar se a mensagem contém pornografia e, caso positivo, apagá-la e banir o usuário que a enviou.

# Para verificar se uma mensagem contém pornografia, podemos usar a biblioteca pyporn. É necessário instalá-la usando o seguinte comando: "pip install pyporn"

# No código acima, a função handle_message é registrada como manipulador de mensagens do bot. Essa função recebe a mensagem enviada pelo usuário e o contexto da mensagem. Dentro da função, verificamos se a mensagem contém pornografia usando a função pyporn.contains_porn. Se a mensagem contiver pornografia, a função remove a mensagem usando context.bot.delete_message e bane o usuário usando context.bot.kick_chat_member.

# Por fim, registramos o manipulador de mensagens usando dispatcher.add_handler e iniciamos o bot usando updater.start_polling().

# Com esse código, o bot irá remover mensagens contendo pornografia e banir usuários que as enviaram em um grupo. Note que essa implementação é baseada em uma biblioteca externa e pode não ser 100% eficaz na detecção de pornografia. Além disso, é importante lembrar que o uso de um bot anti-pornografia pode ser sensível a questões culturais e étnicas, por isso é importante considerar cuidadosamente o seu uso e implementação.