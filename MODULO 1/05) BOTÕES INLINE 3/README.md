# BOTÕES DE INLINE DE URL
Este é um exemplo de um bot do Telegram criado em Python usando a biblioteca Telebot. O bot apresenta botões inline que, quando clicados, abrem URLs específicas.

## Configuração
1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca Telebot executando o seguinte comando em seu terminal:

   ```bash
   pip install pyTelegramBotAPI
   ```

3. Crie um novo bot no Telegram e obtenha o token do bot.

## Uso
1. Substitua `"SEU_TOKEN"` pela token do seu bot na variável `TOKEN`.
2. Substitua `"URL_DO_BOTAO_1"` e `"URL_DO_BOTAO_2"` pelas URLs reais que você deseja usar para os botões.
```python
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "SEU_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton("Botão 1", url="URL_DO_BOTAO_1")
    button2 = InlineKeyboardButton("Botão 2", url="URL_DO_BOTAO_2")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Use os botões inline para acessar os links!", reply_markup=markup)

bot.polling()
```

## Executando o Bot
Após configurar e editar o código com suas informações, você pode executar o bot usando o seguinte comando em seu terminal:
```bash
python nome_do_arquivo.py
```

Substitua `nome_do_arquivo.py` pelo nome do arquivo em que você salvou o código.

## Resultado
O bot enviará uma mensagem com os botões inline para acessar as URLs fornecidas. Ao clicar em um dos botões, o usuário será redirecionado para a URL correspondente.

Certifique-se de ter o token do seu bot e URLs válidas para os botões inline.

**Lembre-se:** Mantenha suas URLs seguras e confiáveis, pois os usuários do bot poderão acessá-las diretamente.

Este exemplo demonstra como criar um bot simples com botões inline no Telegram usando Python e a biblioteca Telebot. Você pode personalizar ainda mais o código para adicionar mais botões ou funcionalidades ao seu bot.