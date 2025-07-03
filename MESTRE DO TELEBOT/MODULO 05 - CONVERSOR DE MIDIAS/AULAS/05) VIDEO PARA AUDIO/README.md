# VIDEO PARA AUDIO MP3
## DESCRIÇÃO:
Este bot responderá a qualquer mensagem de vídeo enviada com um arquivo de áudio MP3 convertido. Ele utiliza a biblioteca python-telegram-bot para interagir com a API do Telegram e a biblioteca moviepy para a manipulação de vídeo e áudio.

## EXPLICAÇÃO:
1. **Importações:**

   * `from TOKEN import *`: Importa o token do bot armazenado no arquivo `TOKEN.py`.
   * `from telegram.ext import Updater, MessageHandler, Filters`: Importa as classes e funções necessárias do framework `python-telegram-bot`:

     * `Updater`: gerencia a conexão com a API do Telegram.
     * `MessageHandler`: permite lidar com tipos específicos de mensagens (como vídeos).
     * `Filters`: usado para filtrar mensagens com certos conteúdos (neste caso, vídeos).
   * `import os`: Importa o módulo `os`, **não é utilizado diretamente nesse código.**
   * `from moviepy.editor import VideoFileClip`: Importa a classe `VideoFileClip` da biblioteca `moviepy`, usada para abrir e manipular vídeos.

2. **Função `convert_video_to_audio`:**

   * Responsável por lidar com mensagens de vídeo e convertê-las para áudio MP3.

3. `video_file = update.message.video.get_file()`:

   * Obtém o arquivo de vídeo enviado pelo usuário através da API do Telegram.

4. `video_file_path = video_file.download('input_video.mp4')`:

   * Baixa o arquivo de vídeo e o salva localmente com o nome `input_video.mp4`.

5. `output_audio_path = 'output_audio.mp3'`:

   * Define o nome do arquivo de saída de áudio.

6. `clip = VideoFileClip(video_file_path)`:

   * Abre o vídeo baixado usando o `moviepy`.

7. `clip.audio.write_audiofile(output_audio_path)`:

   * Extrai a faixa de áudio do vídeo e a salva como `output_audio.mp3` no formato MP3.

8. `context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(output_audio_path, 'rb'))`:

   * Envia o arquivo MP3 gerado de volta ao usuário como mensagem de áudio.

9. **Função `main`:**

   * Responsável por iniciar o bot, registrar os handlers e começar o polling.

10. `updater = Updater(TOKEN, use_context=True)`:

* Cria uma instância do `Updater` usando o token do bot.
* `use_context=True` ativa o modo de contexto moderno (obrigatório nas versões mais recentes da lib).

11. `dp = updater.dispatcher`:

* Obtém o **dispatcher**, que é responsável por encaminhar as mensagens para os handlers corretos.

12. `dp.add_handler(MessageHandler(Filters.video & ~Filters.command, convert_video_to_audio))`:

* Registra um handler que será acionado apenas quando o bot receber mensagens com **vídeos** que **não sejam comandos**.
* As mensagens serão processadas pela função `convert_video_to_audio`.

13. `updater.start_polling()`:

* Inicia o bot no modo *polling*, ou seja, ele ficará verificando constantemente se há novas mensagens.

14. `updater.idle()`:

* Mantém o bot em execução até que seja encerrado manualmente (por exemplo, com `Ctrl + C`).

15. **Bloco Final:**

```python
if __name__ == '__main__':
    main()
```

* Garante que a função `main()` só será executada se o script for rodado diretamente (e não importado como módulo).

## INSTRUÇÃO:
Para criar um bot que converta qualquer foto recebida para o formato `ICO`, você pode usar a biblioteca python-telegram-bot em conjunto com a biblioteca moviepy para manipulação de video e audio. Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py)

Certifique-se de instalar as bibliotecas necessárias antes de executar o código:

```bash
pip install moviepy
```