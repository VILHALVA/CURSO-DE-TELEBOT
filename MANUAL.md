# MANUAL
## INSTALAÇÃO DO PYTHON:
1. **Baixar o Python:** Primeiro, você precisa ter o Python instalado no seu sistema. Se você ainda não tem o Python instalado, siga as instruções abaixo para baixá-lo de acordo com seu sistema operacional:

   - **Windows:** Vá para o site oficial do Python em [python.org](https://www.python.org/downloads/windows/) e baixe a versão mais recente do Python para Windows. Execute o instalador e siga as instruções para instalar o Python.

   - **Linux:** A maioria das distribuições Linux já vem com o Python pré-instalado. No entanto, você pode verificar a versão do Python usando o comando `python3 --version`. Se não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição (por exemplo, `sudo apt-get install python3` no Ubuntu).

   - **macOS:** O macOS também geralmente inclui o Python pré-instalado. Você pode verificar a versão do Python usando o comando `python3 --version`. Se necessário, você pode instalá-lo usando um gerenciador de pacotes como o Homebrew.

## INSTALAÇÃO DA BIBLIOTECA: `pyTelegramBotAPI`:
Depois de ter o Python instalado, você pode instalar a biblioteca `pyTelegramBotAPI` usando o `pip`, que é o gerenciador de pacotes padrão do Python. Abra o terminal ou prompt de comando e execute o seguinte comando:

```bash
pip install pyTelegramBotAPI
```

Isso instalará a biblioteca `pyTelegramBotAPI` no seu ambiente Python.

Agora, você pode começar a criar seu bot em Python e usar a biblioteca `pyTelegramBotAPI` para interagir com a API do Telegram. Certifique-se de obter um token de acesso do BotFather do Telegram antes de criar seu bot e substitua `"SEU_TOKEN_AQUI"` pelo token real do seu bot no código Python.

Com a biblioteca `pyTelegramBotAPI` instalada e o Python configurado, você está pronto para criar e executar seu bot no Telegram.

## CRIANDO O AVATAR DO BOT E EXECUTANDO:
- 1️⃣Entre no privado com [@botfather](https://t.me/botfather) e configure o avatar do seu bot:
   - 🔹`/newbot` - Novo Bot.
   - 🔹`/editname` - Dê o Nome.
   - 🔹`/editabout` - Coloque a Bios.
   - 🔹`/editdescription` - Coloque a Descrição.
   - 🔹`/editbotpic` - Coloque a foto.
   - 🔰SALVE O TOKEN DO SEU BOT.

- 2️⃣Você precisa saber programar em Python. Se não souber, [clique aqui para fazer o curso de Python.](https://github.com/VILHALVA/CURSO-DE-PYTHON)

- 3️⃣Você pode baixar e personalizar esse repositório. [Ou usar alguns exemplos prontos do Telegram.](https://core.telegram.org/bots/samples)

- 4️⃣Ao copiar o código, as únicas coisas gerais que você irá precisar colocar é:
   - 🔰TOKEN DO BOT
   - 🔰ID DO CHAT
   - ✅Pronto: É só executar o código na sua IDE ou no servidor remoto.

## CRIANDO UM PROJETO:
### 1. CÓDIGO PYTHON:
Crie um arquivo Python, por exemplo `meu_bot.py`, e adicione o seguinte código:

```python
import telebot
from TOKEN import TOKEN  # Importe seu token do arquivo TOKEN.py

# Inicializa o bot com o token fornecido pelo BotFather
bot = telebot.TeleBot(TOKEN)

# Manipulador para responder a mensagens de texto
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, f"Olá {message.from_user.first_name}, você enviou: {message.text}")

# Inicia o bot
bot.polling()
```

### 2. ARQUIVO `TOKEN.py`
Crie um arquivo `TOKEN.py` no mesmo diretório do seu script Python `meu_bot.py` com o conteúdo abaixo:

```python
TOKEN = 'seu_token_aqui'
```

Substitua `'seu_token_aqui'` pelo token que você recebeu do BotFather.

### 3. EXECUTE O BOT:
Execute o script `meu_bot.py`. Ele irá iniciar o bot e fazer com que ele fique escutando mensagens enviadas para ele. Quando um usuário enviar uma mensagem, o bot responderá com uma saudação personalizada junto com a mensagem recebida.

### FUNCIONALIDADES:
- **Resposta Automática:** O bot responde a qualquer mensagem de texto enviada a ele com uma saudação personalizada.
- **Configuração Simples:** Utiliza o `pyTelegramBotAPI` para interagir com a API do Telegram de maneira fácil e eficiente.
- **Personalização:** Você pode personalizar as respostas, adicionar mais manipuladores para diferentes tipos de mensagens, e explorar outras funcionalidades oferecidas pelo `pyTelegramBotAPI`.
