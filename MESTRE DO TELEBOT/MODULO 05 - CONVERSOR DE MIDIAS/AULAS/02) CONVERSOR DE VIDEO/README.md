# CONVERSOR DE VIDEO: QUALQUER VIDEO PARA MP4
## DESCRIÇÃO:
Este bot responderá a qualquer mensagem de vídeo enviada com um arquivo MP4 convertido. Ele utiliza a biblioteca python-telegram-bot e o ffmpeg para a conversão.

## EXPLICAÇÃO:
1. **Importação de Bibliotecas:**

   * `import os`: Importa o módulo `os` para executar comandos no sistema, como a chamada ao `ffmpeg` para conversão de vídeo.
   * `from telegram.ext import Updater, MessageHandler, Filters`: Importa os componentes da biblioteca `python-telegram-bot` usados para criar o bot, registrar handlers e filtrar mensagens.
   * `from TOKEN import *`: Importa o token do bot a partir de um arquivo `TOKEN.py`, garantindo que o token esteja separado do código principal.

2. **Função `convert_video_to_mp4`:**

   * **Responsável por processar mensagens com vídeos.**

3. `video_file = update.message.video.get_file()`: Obtém o objeto de arquivo do vídeo enviado pelo usuário.

4. `video_file_path = video_file.download('input_video')`: Faz o download do vídeo para o disco local, com o nome `input_video`.

5. `os.system("ffmpeg -i input_video -c:v copy -c:a aac -strict experimental output_video.mp4")`:

   * Executa um comando `ffmpeg` no terminal para converter o vídeo baixado (`input_video`) para o formato MP4.
   * `-c:v copy`: Copia o vídeo sem recodificar.
   * `-c:a aac`: Codifica o áudio no formato AAC.
   * `-strict experimental`: Permite o uso de recursos experimentais do ffmpeg.
   * O vídeo convertido é salvo como `output_video.mp4`.

6. `context.bot.send_video(chat_id=update.effective_chat.id, video=open('output_video.mp4', 'rb'))`:

   * Envia o vídeo convertido de volta ao usuário.
   * Usa `open(..., 'rb')` para abrir o arquivo em modo binário de leitura.

7. **Função `main`:**

   * Responsável por configurar e iniciar o bot.

8. `updater = Updater(TOKEN, use_context=True)`:

   * Cria o objeto `Updater` com o token do bot e habilita o contexto nos handlers (recomendado nas versões mais recentes da biblioteca).

9. `dp = updater.dispatcher`: Obtém o dispatcher (`dp`) que é usado para adicionar os handlers de mensagens.

10. `dp.add_handler(MessageHandler(Filters.video & ~Filters.command, convert_video_to_mp4))`:

    * Adiciona um `MessageHandler` que responde apenas a mensagens que contenham **vídeo** e **não** sejam comandos.
    * Associa essas mensagens à função `convert_video_to_mp4`.

11. `updater.start_polling()`: Inicia o processo de polling, que escuta continuamente novas mensagens do Telegram.

12. `updater.idle()`: Mantém o bot em execução até que seja manualmente interrompido (como com `Ctrl+C`).

13. **Bloco Condicional `if __name__ == '__main__':`**:

    * Garante que a função `main()` só será executada se o script for rodado diretamente (não importado como módulo).

## INSTRUÇÃO:
Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py). Além disso, você precisará ter o ffmpeg instalado em seu sistema para este bot funcionar.

## COMO INSTALAR O FFMPEG?
**No Windows:**

1. Baixe o FFmpeg do site oficial: [FFmpeg Download](https://ffmpeg.org/download.html).
2. Extraia o arquivo zip para uma pasta de sua escolha.
3. Adicione o diretório binário do FFmpeg ao seu PATH do sistema:
   - Clique com o botão direito do mouse em "Este PC" ou "Meu Computador" e selecione "Propriedades".
   - Clique em "Configurações avançadas do sistema" e, em seguida, em "Variáveis de ambiente".
   - Na seção "Variáveis do sistema", encontre a variável "Path" e clique em "Editar".
   - Adicione o caminho para a pasta bin do FFmpeg (por exemplo, `C:\caminho\para\ffmpeg\bin`) ao final da lista de valores separados por ponto e vírgula.
4. Verifique se o FFmpeg está instalado corretamente abrindo um prompt de comando e digitando `ffmpeg -version`. Se a instalação foi bem-sucedida, você deverá ver a versão do FFmpeg instalada.

**No Linux:**

1. Instale o FFmpeg usando o gerenciador de pacotes do seu sistema. Por exemplo, no Ubuntu, você pode executar o seguinte comando no terminal:
   ```bash
   sudo apt-get install ffmpeg
   ```
2. Verifique se o FFmpeg está instalado corretamente digitando `ffmpeg -version` no terminal. Se a instalação foi bem-sucedida, você deverá ver a versão do FFmpeg instalada.
