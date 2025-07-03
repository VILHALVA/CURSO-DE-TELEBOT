# TEXTO PARA VOZ MP3
## DESCRIÇÃO:
Este bot responderá a qualquer mensagem de texto enviada com um arquivo de áudio MP3 convertido. Ele utiliza a biblioteca python-telegram-bot para interagir com a API do Telegram e a biblioteca gTTS para a conversão de texto em voz.

## EXPLICAÇÃO:
1. **Importações:**

```python
from TOKEN import *
```

* Importa o token de autenticação do bot armazenado no arquivo `TOKEN.py`.

```python
from telegram.ext import Updater, MessageHandler, Filters
```

* Importa componentes da biblioteca `python-telegram-bot` para criar e gerenciar o bot:

  * `Updater`: conecta o bot à API do Telegram.
  * `MessageHandler`: escuta mensagens recebidas.
  * `Filters`: define filtros para tipos específicos de mensagens.

```python
from gtts import gTTS
```

* Importa a classe `gTTS` da biblioteca `gTTS` (Google Text-to-Speech) para converter texto em fala.

```python
import os
```

* Importa o módulo `os` para manipulação do sistema de arquivos (não usado diretamente neste código, mas geralmente útil para operações locais).

2. **Função `convert_text_to_speech`**:

Responsável por converter o texto enviado pelo usuário em áudio MP3 e enviar de volta.

```python
text = update.message.text
```

* Obtém o texto enviado pelo usuário na mensagem.

```python
tts = gTTS(text=text, lang='pt-br')
```

* Cria um objeto `gTTS` com o texto recebido, configurando o idioma para português do Brasil (`pt-br`).

```python
tts.save('output_audio.mp3')
```

* Salva o áudio gerado no arquivo local `output_audio.mp3`.

```python
context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('output_audio.mp3', 'rb'))
```

* Envia o arquivo de áudio gerado para o mesmo chat onde o texto foi recebido.

3. **Função principal `main`** — configuração do bot:

```python
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
```

* Inicializa o objeto `Updater` com o token do bot e obtém o `dispatcher` para registrar handlers.

```python
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, convert_text_to_speech))
```

* Adiciona um handler que escuta mensagens de texto que **não sejam comandos** e chama `convert_text_to_speech` para processar.

```python
updater.start_polling()
updater.idle()
```

* Inicia o bot para ficar escutando mensagens e mantém o bot ativo até que seja manualmente interrompido.

4. **Bloco principal para execução direta:**

```python
if __name__ == '__main__':
    main()
```

* Garante que a função `main()` só será executada se o script for rodado diretamente (não importado como módulo).

## INSTRUÇÃO:
Para criar um bot que converta qualquer texto recebido para audio no formato `MP3`, você pode usar a biblioteca python-telegram-bot em conjunto com a biblioteca gtts para conversão. Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py)

Certifique-se de instalar as bibliotecas necessárias antes de executar o código:

```bash
pip install gtts
```