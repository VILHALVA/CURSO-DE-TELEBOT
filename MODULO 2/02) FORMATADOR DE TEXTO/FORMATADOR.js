const TelegramBot = require('node-telegram-bot-api');
const token = 'SEU_TOKEN_AQUI';
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  const instructions = `
Bem-vindo ao FormatBot! ✨

Este bot permite que você formate seu texto de maneiras criativas. 
Aqui estão algumas das formatações disponíveis:

*grassetto* - **grassetto**
_corsivo_ - _corsivo_
\`code\` - \`code\`
[Google](https://www.google.com) - [Google](https://www.google.com/)
%blu% - 🇧 🇱 🇺
-barrato- - ~~barrato~~
;sottolineato; - sottolineato
^grande^ - ｇｒａｎｄｅ
&maiuscoletto& - ᴍᴀɪᴜsᴄᴏʟᴇᴛᴛᴏ
@bolle@ - ⒷⓄⓁⓁⒺ

Envie a mensagem que você deseja formatar e veja a mágica acontecer!
`;
  bot.sendMessage(chatId, instructions, { parse_mode: 'Markdown' });
});

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;

  // Formatação do texto
  let formattedText = text;
  formattedText = formattedText.replace(/\*(.*?)\*/g, '*$1*');
  formattedText = formattedText.replace(/_(.*?)_/g, '_$1_');
  formattedText = formattedText.replace(/`(.*?)`/g, '`$1`');
  formattedText = formattedText.replace(/\[(.*?)\]\((.*?)\)/g, '[$1]($2)');
  formattedText = formattedText.replace(/-(.*?)-/g, '~~$1~~');
  formattedText = formattedText.replace(/;(.*?);/g, 's̲$1');
  formattedText = formattedText.replace(/\^(.*?)\^/g, 'ｇｒａｎｄｅ');
  formattedText = formattedText.replace(/&([^&]*)&/g, 'ᴍᴀɪᴜsᴄᴏʟᴇᴛᴛᴏ');
  formattedText = formattedText.replace(/@([^@]*)@/g, 'ⒷⓄⓁⓁⒺ');
  formattedText = formattedText.replace(/%([^%]*)%/g, '*$1*');

  bot.sendMessage(chatId, formattedText, { parse_mode: 'Markdown' });
});
