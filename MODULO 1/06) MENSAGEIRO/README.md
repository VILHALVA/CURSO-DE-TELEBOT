# BOTS DE RECADOS
## RECADOS V.1
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

## RECADOS V.2
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

## RECADOS V.3
Este é um bot de Telegram em Python que permite enviar mensagens de recados para grupos e usuários que se inscreveram para receber essas mensagens.

## Funcionalidades
- Os usuários podem iniciar uma conversa com o bot e se inscrever para receber mensagens de recados.
- O administrador do bot pode enviar mensagens de recados para todos os inscritos.

## Como Usar
1. Crie um novo bot no Telegram através do [BotFather](https://core.telegram.org/bots#botfather) e obtenha o token do bot.

2. Substitua `'YOUR_BOT_TOKEN'` pelo token do seu bot no código.

3. Determine o ID do usuário administrador que terá permissão para enviar mensagens de recados. Substitua `YOUR_ADMIN_USER_ID` pelo ID desse usuário no código.

4. Instale a biblioteca `python-telegram-bot` se ainda não a tiver instalado:

```bash
pip install python-telegram-bot
```

5. Execute o código Python para iniciar o bot:

```bash
python bot_de_recados.py
```

## Comandos Disponíveis
- `/start`: Os usuários podem usar este comando para se inscreverem para receber mensagens de recados.

- `/send <mensagem>`: O administrador do bot pode usar este comando seguido pela mensagem que deseja enviar para todos os inscritos.

## Observações
Certifique-se de que o bot foi adicionado a todos os grupos em que você deseja enviar mensagens de recados e que os usuários iniciaram uma conversa com o bot para que possam receber as mensagens.

Lembre-se de que este bot enviará mensagens apenas para os grupos e usuários que se inscreveram para receber mensagens de recados. Certifique-se de usar o comando `/start` para se inscrever antes de usar o comando `/send`.

Este bot é destinado a fins educacionais e demonstrativos. Certifique-se de usar o bot de maneira responsável e respeitando as políticas de uso do Telegram.
