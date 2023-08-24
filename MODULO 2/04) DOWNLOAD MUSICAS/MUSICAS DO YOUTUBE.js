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

