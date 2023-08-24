# BOTÕES DE TECLADO (COMO O MANYBOT)
Este é um guia passo a passo para criar um bot do Telegram em Python que utiliza botões de teclado de resposta para interações simples com os usuários. Os botões de teclado de resposta são uma maneira eficaz de fornecer opções pré-definidas para que eles possam selecionar uma resposta com apenas um toque, tornando a interação mais intuitiva e amigável.

### Pré-requisitos
1. **Token do Bot:** Para começar, você precisará do token do seu bot do Telegram. Se você ainda não possui um bot, você pode criar um falando com o [BotFather](https://core.telegram.org/bots#botfather) no Telegram.

### Instalação
Antes de prosseguir, você precisará instalar a biblioteca `python-telegram-bot`. Você pode instalar esta biblioteca usando o seguinte comando:
```bash
pip install python-telegram-bot
```

### Código de Exemplo
Aqui está um exemplo de código que demonstra como criar um bot do Telegram em Python com botões de teclado de resposta:
```python
import telebot
from telebot import types

TOKEN = "SEU_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Opção 1")
    item2 = types.KeyboardButton("Opção 2")
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, "Escolha uma opção:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Opção 1":
        bot.send_message(message.chat.id, "Você selecionou a Opção 1.")
    elif message.text == "Opção 2":
        bot.send_message(message.chat.id, "Você selecionou a Opção 2.")
    else:
        bot.send_message(message.chat.id, "Por favor, escolha uma das opções.")

bot.polling()
```

### Executando o Bot
Após criar e salvar o código acima em um arquivo Python, você pode executá-lo para iniciar o bot. Quando você enviar o comando `/start` para o bot, ele responderá com um teclado de resposta contendo as opções "Opção 1" e "Opção 2". Ao selecionar uma das opções, o bot enviará uma mensagem de resposta correspondente.

**Nota:** Lembre-se de que o uso de botões de teclado de resposta é uma ótima maneira de melhorar a interação com os usuários, mas certifique-se de que os botões sejam claros e relevantes para a conversa.

Com essas informações, você pode criar bots mais interativos e envolventes usando botões de teclado de resposta no Telegram. Certifique-se de experimentar e personalizar o código conforme suas necessidades!