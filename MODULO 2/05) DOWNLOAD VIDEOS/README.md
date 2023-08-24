# DOWNLOAD VIDEOS
## JAVASCRIPT
Para criar um bot do Telegram em JavaScript, podemos usar a biblioteca Telegraf.js. O Telegraf.js é uma biblioteca simples e poderosa que nos permite criar bots do Telegram em JavaScript de maneira fácil e rápida.

Nesse código, usamos a biblioteca axios para fazer uma solicitação GET ao servidor do YouTube para obter o link do vídeo completo a partir do ID do vídeo. Usamos o módulo url do Node.js para analisar a URL do vídeo e obter o ID do vídeo. Também definimos duas funções, isYoutubeUrl e getVideoId, para verificar se a URL do YouTube é válida e obter o ID do vídeo.

Certifique-se de substituir YOUR_TELEGRAM_BOT_TOKEN pelo token do seu bot do Telegram. Você pode obter o token do seu bot do Telegram conversando com o BotFather.

## PYTHON
Para criar um bot do Telegram em Python que possa receber um link do YouTube e enviar o vídeo completo de volta, você precisará seguir os seguintes passos:
Criar um bot no Telegram e obter seu token de acesso.
Instalar a biblioteca python-telegram-bot.
Escrever um código que lida com a mensagem enviada pelo usuário e extrai o link do YouTube.
Usar a biblioteca pytube para baixar o vídeo do YouTube.
Enviar o vídeo baixado de volta para o usuário.