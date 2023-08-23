# BOT DE RECADOS
## VERSÃO 1
Este é um bot para Telegram desenvolvido em Python, usando a biblioteca telebot, que permite enviar recados para grupos do Telegram.

### Pré-requisitos
- [Python](https://www.python.org/) (versão 3.6 ou superior)
- Biblioteca telebot (`pip install pyTelegramBotAPI`)

### Configuração
1. Crie um novo bot no Telegram através do [BotFather](https://core.telegram.org/bots#botfather) e obtenha o token do bot.
2. Clone este repositório para a sua máquina local.
3. Substitua `"SEU_TOKEN_AQUI"` pelo token do seu bot no código.
4. Dentro do ``chat_id`` coloque o id do seu grupo.
5. Dentro do ``bot.send_message(chat_id, '''TEXTO''')`` coloque a mensagem que deverá ser enviada.

## VERSÃO 2
Este é um exemplo de um bot do Telegram que utiliza a biblioteca `telebot` para se comunicar com a API do Telegram e uma interface gráfica criada com `tkinter` para interagir com o bot. O bot é capaz de receber mensagens do usuário e responder a elas. As mensagens enviadas e recebidas são exibidas em uma interface gráfica simples.

### Pré-requisitos
Certifique-se de ter as bibliotecas `pyTelegramBotAPI` e `tkinter` instaladas. Você pode instalá-las usando o seguinte comando:

```
pip install pyTelegramBotAPI tkinter
```

### Como Usar?
1. Clone este repositório ou baixe o código-fonte.

2. Substitua `"SEU_TOKEN_AQUI"` pelo token do seu bot na variável `TOKEN`.

3. Substitua `"ID_DO_CHAT_AQUI"` pelo ID do chat ou grupo no qual você deseja que o bot responda.

4. Execute o script Python:

```
python telegram_bot_with_gui.py
```

5. Uma janela do tkinter será aberta. Você pode digitar mensagens na entrada e clicar no botão "Enviar". O bot irá responder às mensagens na própria janela.

### Funcionalidades
- O bot é capaz de responder a qualquer mensagem que você digitar na interface gráfica.
- As mensagens enviadas e recebidas são exibidas na janela.
- A interface gráfica inclui uma entrada para digitar mensagens e um botão para enviá-las.

