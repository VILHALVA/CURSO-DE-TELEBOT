const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');

const TOKEN = 'SEU_TOKEN';
const bot = new TelegramBot(TOKEN, { polling: true });

const PEXELS_API_KEY = 'SUA_CHAVE_DO_PEXELS';

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, 'Olá! Envie uma descrição de uma imagem ou uma palavra-chave.');
});

bot.onText(/.*/, async (msg, match) => {
  const chatId = msg.chat.id;
  const query = match[0];
  const pexelsApiUrl = `https://api.pexels.com/v1/search?query=${encodeURIComponent(query)}&per_page=1`;
  
  try {
    const response = await axios.get(pexelsApiUrl, {
      headers: {
        Authorization: PEXELS_API_KEY,
      },
    });

    if (response.status === 200 && response.data.photos.length > 0) {
      const imageUrl = response.data.photos[0].src.original;
      bot.sendPhoto(chatId, imageUrl);
    } else {
      bot.sendMessage(chatId, 'Não foi possível encontrar uma imagem correspondente.');
    }
  } catch (error) {
    bot.sendMessage(chatId, 'Ocorreu um erro ao buscar a imagem.');
  }
});
