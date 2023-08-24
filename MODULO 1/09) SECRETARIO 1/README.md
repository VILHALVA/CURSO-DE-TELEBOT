# SECRETARIO BOT
Este é um exemplo simples de como criar um bot do Telegram em Python usando a biblioteca `python-telegram-bot`. O bot recebe mensagens de texto dos usuários, extrai informações sobre o usuário e encaminha a mensagem para um chat privado do Telegram.

## Requisitos
Certifique-se de ter instalado o Python em sua máquina. Além disso, você precisará instalar a biblioteca `python-telegram-bot` para interagir com a API do Telegram. Você pode instalar a biblioteca usando o seguinte comando:
```bash
pip install python-telegram-bot
```

## Configuração
1. Crie um bot no Telegram e obtenha o token do bot do BotFather.

2. Substitua `'YOUR_BOT_TOKEN'` na linha `token = 'YOUR_BOT_TOKEN'` pelo token real do seu bot.

## Executando o Bot
1. Execute o script Python. O bot começará a receber mensagens de texto dos usuários.

2. Quando um usuário enviar uma mensagem de texto para o bot, o bot extrairá informações sobre o usuário (nome e foto de perfil) e encaminhará a mensagem para um chat privado.

## Código de Exemplo
```python
import asyncio
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Obtém o token do bot do BotFather
token = 'YOUR_BOT_TOKEN'

# Cria um updater para o bot
updater = Updater(token=token)

# Define um manipulador de mensagens
def handle_message(update, context):
    # Obtém o texto da mensagem
    text = update.message.text

    # Obtém o nome e a foto de perfil do usuário
    user = update.effective_user
    name = user.full_name
    avatar = user.profile_photo

    # Envia a mensagem para o nosso privado
    updater.bot.send_message(chat_id=updater.bot.get_me().id, text=f'**{name}:** {text}')

# Registra os manipuladores de mensagens
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Inicia o bot
updater.start_polling()
updater.idle()
```

## Personalização
Este é um exemplo básico para começar a criar um bot do Telegram em Python. Você pode personalizar e expandir o bot adicionando mais manipuladores de mensagens, comandos e funcionalidades, conforme necessário.

## Documentação
- [python-telegram-bot Documentation](https://python-telegram-bot.readthedocs.io/en/stable/index.html): Documentação oficial da biblioteca `python-telegram-bot`.

Lembre-se de que este é um exemplo básico e pode ser usado como ponto de partida para criar bots mais complexos e interativos.