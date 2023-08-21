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




