const Telegraf = require('telegraf');
const axios = require('axios');
const url = require('url');

const bot = new Telegraf('seu_token_aqui');

bot.start((ctx) => ctx.reply('Bem-vindo ao bot do YouTube! Envie-me um link do YouTube para obter o vídeo completo.'));

bot.on('text', (ctx) => {
  const youtubeUrl = ctx.message.text;
  if (isYoutubeUrl(youtubeUrl)) {
    const videoId = getVideoId(youtubeUrl);
    axios.get(`https://www.youtube.com/get_video_info?video_id=${videoId}&el=detailpage`)
      .then(response => {
        const data = url.parse(`http://www.youtube.com${response.data}`);
        const videoUrl = decodeURIComponent(data.query.split('&url=')[1]);
        ctx.replyWithVideo(videoUrl);
      })
      .catch(error => {
        console.error(error);
        ctx.reply('Desculpe, não foi possível encontrar o vídeo.');
      });
  } 
  
  else {
    ctx.reply('Por favor, envie um link válido do YouTube.');
  }
});

function isYoutubeUrl(url) {
  const pattern = /^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)[\w-]{11}$/;
  return pattern.test(url);
}

function getVideoId(url) {
  const parsedUrl = url.parse(url);
  if (parsedUrl.hostname === 'youtu.be') {
    return parsedUrl.pathname.substr(1);
  } 
  
  else {
    const query = parsedUrl.query.substr(parsedUrl.query.indexOf('?') + 1);
    const params = query.split('&');
    for (let i = 0; i < params.length; i++) {
      const param = params[i].split('=');
      if (param[0] === 'v') {
        return param[1];
      }
    }
  }
}
bot.launch();

// Para criar um bot do Telegram em JavaScript, podemos usar a biblioteca Telegraf.js. O Telegraf.js é uma biblioteca simples e poderosa que nos permite criar bots do Telegram em JavaScript de maneira fácil e rápida.

// Nesse código, usamos a biblioteca axios para fazer uma solicitação GET ao servidor do YouTube para obter o link do vídeo completo a partir do ID do vídeo. Usamos o módulo url do Node.js para analisar a URL do vídeo e obter o ID do vídeo. Também definimos duas funções, isYoutubeUrl e getVideoId, para verificar se a URL do YouTube é válida e obter o ID do vídeo.

// Certifique-se de substituir YOUR_TELEGRAM_BOT_TOKEN pelo token do seu bot do Telegram. Você pode obter o token do seu bot do Telegram conversando com o BotFather.


