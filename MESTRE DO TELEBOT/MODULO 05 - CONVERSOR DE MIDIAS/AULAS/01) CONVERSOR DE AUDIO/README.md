# CONVERSOR DE AUDIO: QUALQUER AUDIO PARA MP3
## DESCRIÇÃO:
Este é um bot do que converte qualquer mensagem de áudio recebida para o formato MP3 e a envia de volta ao usuário. Ele usa a biblioteca pydub para manipular o áudio.

## EXPLICAÇÃO:
```python
from io import BytesIO
from pydub import AudioSegment
from telegram.ext import Updater, MessageHandler, Filters
from TOKEN import *
```

* Importa a classe `BytesIO`, que permite criar e manipular dados binários na memória como se fossem arquivos. Será usada para armazenar temporariamente o áudio.
* Importa a classe `AudioSegment` da biblioteca `pydub`, que permite manipular e converter arquivos de áudio de/para diversos formatos (como WAV, MP3, etc.).
* Importa:
  * `Updater`: objeto que gerencia a conexão com a API do Telegram.
  * `MessageHandler`: lida com mensagens recebidas, aplicando filtros.
  * `Filters`: permite definir filtros para o tipo de mensagem (ex: `audio`, `text`, etc.).
* Importa o token do bot a partir de um arquivo chamado `TOKEN.py`, onde está definido algo como `TOKEN = 'seu_token_aqui'`.

```python
# Função para converter o áudio para MP3
def convert_to_mp3(audio_data):
```

* Define a função `convert_to_mp3`, que recebe os dados de um áudio e retorna a versão convertida em MP3.

```python
    # Carrega o áudio na memória
    audio = AudioSegment.from_file(BytesIO(audio_data))
```

* Converte os dados binários em um objeto `AudioSegment`, como se fosse um arquivo de áudio. Usa `BytesIO` para transformar os dados brutos em um "arquivo" temporário.

```python
    # Cria um buffer para armazenar o áudio convertido
    output_buffer = BytesIO()
```

* Cria um novo `BytesIO` que servirá de saída: um buffer onde o áudio convertido em MP3 será armazenado.

```python
    # Exporta o áudio para MP3 e salva no buffer
    audio.export(output_buffer, format="mp3")
```

* Exporta o áudio (carregado antes) para o formato MP3, salvando diretamente no `output_buffer`.

```python
    # Retorna os dados do áudio convertido
    return output_buffer.getvalue()
```

* Retorna os dados binários do áudio MP3, que poderão ser enviados pelo bot.

---

```python
# Função para lidar com mensagens de áudio
def handle_audio(update, context):
```

* Define uma função que será chamada toda vez que o bot receber uma mensagem com um arquivo de áudio.

```python
    # Verifica se a mensagem contém um arquivo de áudio
    if update.message.audio:
```

* Verifica se a mensagem recebida possui um campo `audio`, ou seja, se é um áudio carregado via Telegram.

```python
        # Obtém os dados do arquivo de áudio
        audio_file = update.message.audio.get_file()
```

* Usa o método `get_file()` para obter o objeto `File` correspondente ao áudio enviado pelo usuário.

```python
        # Baixa os dados do áudio
        audio_data = audio_file.download_as_bytearray()
```

* Faz o download do áudio e o armazena como uma sequência de bytes (`bytearray`).

```python
        # Converte o áudio para MP3
        mp3_data = convert_to_mp3(audio_data)
```

* Converte os dados do áudio original (independente do formato) para MP3, usando a função definida anteriormente.

```python
        # Envia o áudio convertido de volta ao usuário
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=BytesIO(mp3_data))
```

* Envia o áudio convertido (armazenado em `mp3_data`) de volta ao chat de origem.

---

```python
def main():
```

* Define a função principal que irá inicializar o bot.

```python
    # Crie um objeto Updater e passe seu token bot
    updater = Updater(TOKEN, use_context=True)
```

* Cria o objeto `Updater` e passa o token de autenticação do bot. `use_context=True` ativa o novo sistema baseado em `context`.

```python
    # Obtenha o dispatcher para registrar manipuladores
    dp = updater.dispatcher
```

* Acessa o `dispatcher`, que permite registrar manipuladores de comandos e mensagens.

```python
    # Adicione um manipulador para mensagens de áudio
    dp.add_handler(MessageHandler(Filters.audio, handle_audio))
```

* Adiciona um `MessageHandler` que irá escutar **somente mensagens de áudio** e redirecionar para a função `handle_audio`.

## INSTRUÇÃO:
Para criar um bot que converta qualquer áudio recebido para o formato MP3, você pode usar a biblioteca python-telegram-bot em conjunto com a biblioteca pydub para manipulação de áudio. Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py)

Certifique-se de instalar as bibliotecas necessárias antes de executar o código:

```bash
pip install python-telegram-bot pydub 
```