const TelegramBot = require('node-telegram-bot-api');

// Configuração do bot
const botToken = 'seu_token_aqui';
const bot = new TelegramBot(botToken, { polling: true });

// Função para lidar com a consulta do botão
bot.on('callback_query', (query) => {
  bot.answerCallbackQuery(query.id);
  bot.sendMessage(query.message.chat.id, 'Você clicou no botão!');
});

// Função para enviar a mensagem com o botão inline
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  const keyboard = {
    inline_keyboard: [
      [{ text: 'Clique aqui', callback_data: 'button_clicked' }]
    ]
  };
  const message = 'Clique no botão abaixo:';
  bot.sendMessage(chatId, message, { reply_markup: keyboard });
});

