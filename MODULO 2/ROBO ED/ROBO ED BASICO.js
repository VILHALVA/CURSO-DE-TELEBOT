const { Telegraf } = require('telegraf');

// Criação do objeto bot
const bot = new Telegraf('TOKEN AQUI');

// Define uma função que responde às mensagens do usuário
bot.on('text', (ctx) => {
  const message = ctx.message.text;
  const response = generateResponse(message);
  ctx.reply(response);
});

// Define uma função que gera a resposta do bot
function generateResponse(message) {
  if (message.startsWith('Oi') || message.startsWith('Olá')) {
    return 'Olá, como posso ajudá-lo?';
  } 
  else if (message.startsWith('Como você está?')) {
    return 'Estou bem, obrigado!';
  } 
  else if (message.startsWith('O que você pode fazer?')) {
    return 'Posso responder a perguntas simples e conversar com você.';
  } 
  else if (message.startsWith('Tchau')) {
    return 'Até mais!';
  } 
  else {
    return 'Desculpe, eu não entendi. Você pode reformular a sua pergunta?';
  }
}

// Inicia o bot
bot.launch();

