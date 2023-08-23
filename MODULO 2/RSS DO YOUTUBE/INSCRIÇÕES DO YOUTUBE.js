const {google} = require('googleapis');
const TelegramBot = require('node-telegram-bot-api');

// Chave de autenticação da API do YouTube
const youtubeApiKey = 'YOUR_YOUTUBE_API_KEY';

// Token de acesso do bot do Telegram
const telegramToken = 'YOUR_TELEGRAM_BOT_TOKEN';

// ID do chat do Telegram onde serão enviados os vídeos
const telegramChatId = 'YOUR_TELEGRAM_CHAT_ID';

// Cria um cliente para acessar a API do YouTube
const youtubeClient = google.youtube({
  version: 'v3',
  auth: youtubeApiKey,
});

// Cria um bot do Telegram
const telegramBot = new TelegramBot(telegramToken, {polling: true});

// Lista de IDs dos canais do YouTube em que o usuário está inscrito
const youtubeChannelIds = ['CHANNEL_ID_1', 'CHANNEL_ID_2', 'CHANNEL_ID_3'];

// Obtém os últimos vídeos dos canais do YouTube
async function getLatestVideos() {
  const videos = [];

  for (const channelId of youtubeChannelIds) {
    const response = await youtubeClient.search.list({
      part: 'id',
      channelId,
      order: 'date',
      type: 'video',
      maxResults: 1,
    });

    if (response.data.items.length > 0) {
      const videoId = response.data.items[0].id.videoId;
      videos.push(`https://www.youtube.com/watch?v=${videoId}`);
    }
  }

  return videos;
}

// Envia os vídeos para o chat do Telegram
async function sendVideos(videos) {
  for (const video of videos) {
    await telegramBot.sendMessage(telegramChatId, video);
  }
}

// Verifica periodicamente se há novos vídeos e envia para o chat do Telegram
async function checkForNewVideos() {
  const videos = await getLatestVideos();

  if (videos.length > 0) {
    await sendVideos(videos);
  }
}

