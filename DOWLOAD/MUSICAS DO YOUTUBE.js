const TelegramBot = require('node-telegram-bot-api');
const ytdl = require('youtube-mp3-downloader');
const token = 'seu_token_aqui';

// Configurações do bot
const bot = new TelegramBot(token, { polling: true });

// Configurações do youtube-mp3-downloader
const downloader = new ytdl({
  'ffmpegPath': '/usr/bin/ffmpeg', // caminho do ffmpeg (deve ser instalado no sistema)
  'outputPath': './audios', // diretório de saída dos áudios
  'youtubeVideoQuality': 'highest', // qualidade do vídeo do YouTube
  'queueParallelism': 2, // número de downloads paralelos
  'progressTimeout': 2000 // tempo de atualização do progresso do download
});

// Ao receber uma mensagem com um link do YouTube
bot.on('message', (msg) => {
  if (msg.text.match(/https:\/\/www\.youtube\.com\/watch\?v=.+/)) { // verifica se a mensagem é um link do YouTube
    const chatId = msg.chat.id;
    const youtubeUrl = msg.text;
    downloader.download(youtubeUrl); // inicia o download do áudio do vídeo do YouTube

    downloader.on('finished', function(err, data) { // quando o download terminar
      if (err) throw err;
      bot.sendAudio(chatId, data.file); // envia o arquivo de áudio para o usuário
    });

    downloader.on('error', function(err, data) { // em caso de erro no download
      console.log(err.stack);
    });
  }
});

// Para criar um bot do Telegram em JavaScript que envia a música correspondente ao link do YouTube enviado pelo usuário, é necessário utilizar uma API de conversão de vídeo para áudio. Uma das opções é o "youtube-mp3-downloader".

// Este código utiliza o "node-telegram-bot-api" para a comunicação com o Telegram e o "youtube-mp3-downloader" para a conversão do vídeo em áudio. É necessário instalar estas dependências via npm antes de executar o código.

// Lembrando que a conversão de vídeo para áudio pode ser considerada uma violação dos termos de uso do YouTube, por isso é importante verificar a legislação local e os termos de uso da plataforma antes de utilizar este tipo de recurso.