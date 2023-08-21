const TelegramBot = require('node-telegram-bot-api');
const token = 'seu_token_aqui';
const bot = new TelegramBot(token, {polling: true});

bot.on('message', (msg) => {
  // Verifica se a mensagem vem de um grupo
  if (msg.chat.type === 'group') {
    // Verifica se a mensagem contém pornografia
    if (msg.photo || msg.video || msg.animation || msg.sticker) {
      // Remove a mensagem
      bot.deleteMessage(msg.chat.id, msg.message_id);
      // Bane o membro
      bot.kickChatMember(msg.chat.id, msg.from.id);
    }
  }
});

