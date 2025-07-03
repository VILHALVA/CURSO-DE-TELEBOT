# VOZ PARA TEXTO
## DESCRIÇÃO:
Este bot responderá a qualquer mensagem de voz enviada com o texto reconhecido. Ele utiliza a biblioteca python-telegram-bot para interagir com a API do Telegram e a biblioteca google-cloud-speech para a conversão de voz em texto.

## EXPLICAÇÃO:

1. **Importações e Configurações:**

```python
from TOKEN import *
```

* Importa o token do bot guardado em `TOKEN.py`.

```python
from telegram.ext import Updater, MessageHandler, Filters
```

* Importa módulos do `python-telegram-bot` para criar o bot e escutar mensagens.

```python
from google.cloud import speech
```

* Importa o cliente da API Google Cloud Speech para reconhecimento de voz.

```python
import os
```

* Importa o módulo para manipular variáveis e arquivos do sistema.

2. **Configuração das credenciais do Google Cloud:**

```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "caminho/para/seu/arquivo-de-credenciais.json"
```

* Define a variável de ambiente para o caminho do arquivo JSON que contém as credenciais da sua conta Google Cloud, necessário para autenticar chamadas à API de reconhecimento de voz.

3. **Função `convert_audio_to_text`:**

Responsável por receber o áudio, processá-lo e enviar o texto reconhecido.

```python
voice_file = update.message.voice.get_file()
```

* Obtém o arquivo de voz enviado pelo usuário.

```python
voice_file_path = voice_file.download('input_audio.ogg')
```

* Baixa o arquivo de áudio e salva localmente como `input_audio.ogg`.

```python
client = speech.SpeechClient()
```

* Inicializa o cliente da API Google Speech para fazer as requisições.

```python
with open(voice_file_path, "rb") as audio_file:
    content = audio_file.read()
```

* Abre o arquivo de áudio salvo e lê seu conteúdo em bytes.

```python
audio = speech.RecognitionAudio(content=content)
```

* Cria um objeto de áudio para a requisição da API, usando os bytes carregados.

```python
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
    language_code="pt-BR"
)
```

* Configura as opções de reconhecimento:

  * Especifica que o áudio está codificado em `OGG_OPUS` (formato do áudio do Telegram).
  * Define o idioma como português brasileiro (`pt-BR`).

```python
response = client.recognize(config=config, audio=audio)
```

* Envia a requisição para a API de reconhecimento de fala e armazena a resposta.

```python
for result in response.results:
    context.bot.send_message(chat_id=update.effective_chat.id, text=result.alternatives[0].transcript)
```

* Para cada resultado retornado, extrai a melhor transcrição (alternativa 0) e envia como mensagem para o chat onde o áudio foi recebido.

4. **Função principal `main`:**

```python
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
```

* Inicializa o bot com o token e obtém o dispatcher para gerenciar handlers.

```python
dp.add_handler(MessageHandler(Filters.voice & ~Filters.command, convert_audio_to_text))
```

* Adiciona um handler para capturar mensagens do tipo voz que não sejam comandos, acionando `convert_audio_to_text`.

```python
updater.start_polling()
updater.idle()
```

* Inicia o bot para escutar mensagens e mantém ele rodando.

5. **Bloco de execução direta:**

```python
if __name__ == '__main__':
    main()
```

* Executa `main()` apenas se o script for rodado diretamente, não quando importado.

## INSTRUÇÃO:
Para criar um bot que converte áudio em texto, você pode usar serviços de reconhecimento de fala, como o Google Cloud Speech-to-Text. Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py)

Você precisa configurar as credenciais do Google Cloud e fornecer o caminho para o arquivo JSON de credenciais na variável de ambiente GOOGLE_APPLICATION_CREDENTIALS.