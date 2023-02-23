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

// Para criar um bot do Telegram em JavaScript que permite enviar um texto e receber um áudio com a voz do Ricardo ou Felipe, podemos utilizar a API do Google Cloud Text-to-Speech, que permite converter texto em fala.

// Antes de começar, é necessário criar uma conta no Google Cloud e configurar as credenciais de acesso à API. Em seguida, vamos utilizar a biblioteca node-telegram-bot-api para criar o bot e receber as mensagens dos usuários.

// No código acima, a função textToSpeechHandler recebe um texto e o nome da voz que deve ser usada na conversão para fala. Neste exemplo, estamos utilizando as vozes "pt-BR-Wavenet-B" e "pt-BR-Wavenet-F", que correspondem às vozes do Ricardo e do Felipe, respectivamente. Você pode conferir outras vozes disponíveis na documentação da API do Google Cloud Text-to-Speech.

// A função bot.on('message', ...), registrada como um handler para mensagens, é executada sempre que o bot recebe uma mensagem de texto de um usuário. Essa função converte o texto em fala usando a voz do Ricardo e envia o áudio como mensagem de voz para o usuário.

// Para utilizar a voz do Felipe, basta alterar o segundo parâmetro da função textToSpeechHandler para 'pt-BR-Wavenet-F'.
