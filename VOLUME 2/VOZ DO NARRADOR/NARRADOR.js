const TelegramBot = require('node-telegram-bot-api');
const textToSpeech = require('@google-cloud/text-to-speech');
const fs = require('fs');

// Configuração do bot
const botToken = 'seu_token_aqui';
const bot = new TelegramBot(botToken, { polling: true });

// Configuração do Google Cloud Text-to-Speech
const credentialsPath = 'CAMINHO_DO_ARQUIVO_DE_CREDENCIAIS_AQUI.json';
const client = new textToSpeech.TextToSpeechClient({ keyFilename: credentialsPath });

// Função para converter texto em fala
async function textToSpeechHandler(text, voiceName) {
  const request = {
    input: { text: text },
    voice: { languageCode: 'pt-BR', name: voiceName },
    audioConfig: { audioEncoding: 'MP3' },
  };
  const [response] = await client.synthesizeSpeech(request);
  return response.audioContent;
}

// Função para receber mensagens dos usuários
bot.on('message', async (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;
  const audioData = await textToSpeechHandler(text, 'pt-BR-Wavenet-B');
  bot.sendVoice(chatId, audioData);
});

