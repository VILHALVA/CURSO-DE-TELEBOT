const TelegramBot = require('telegram-bot-api');
const dialogflow = require('dialogflow');
require('dotenv').config();

const TELEGRAM_TOKEN = process.env.TELEGRAM_TOKEN;
const PROJECT_ID = process.env.DIALOGFLOW_PROJECT_ID;
const SESSION_ID = 'telegram-bot';

const bot = new TelegramBot({
  token: TELEGRAM_TOKEN,
  updates: {
    enabled: true,
  },
});

bot.on('message', async (message) => {
  const text = message.text;
  const chatId = message.chat.id;

  // Envia a mensagem para o Dialogflow
  const sessionClient = new dialogflow.SessionsClient();
  const sessionPath = sessionClient.sessionPath(PROJECT_ID, SESSION_ID);
  const request = {
    session: sessionPath,
    queryInput: {
      text: {
        text: text,
        languageCode: 'pt-BR',
      },
    },
  };
  const response = await sessionClient.detectIntent(request);
  const result = response[0].queryResult;

  // Envia a resposta do Dialogflow para o Telegram
  bot.sendMessage({
    chat_id: chatId,
    text: result.fulfillmentText,
  });
});

console.log('Bot is running!');

