const { Telegraf } = require('telegraf');

// Criação do objeto bot
const bot = new Telegraf('seu_token_aqui');

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

// Para criar um bot para o Telegram em JavaScript, podemos utilizar a biblioteca Telegraf, que oferece uma interface simples e intuitiva para interagir com a API do Telegram.

// No código acima, criamos uma função que responde a cada mensagem enviada pelo usuário com uma resposta gerada pela função generateResponse. A função generateResponse verifica a mensagem do usuário e retorna uma resposta apropriada.

// Em seguida, criamos o objeto bot com o token do seu bot do Telegram e adicionamos um listener para o evento text usando o método on. Esse listener é acionado sempre que o bot recebe uma mensagem de texto.

// Por fim, iniciamos o bot usando o método launch(). Certifique-se de substituir 'SEU_TOKEN_DO_BOT' pelo token do seu bot do Telegram.

// AVISO: Não é possível se conectar diretamente com o Robô ED da Petrobras, pois niguém tem acesso às suas APIs ou plataformas de comunicação, como modelo de linguagem. Robôs não podem interagir diretamente com outros robôs ou serviços sem a devida integração e autorização. Sem acesso às APIs e recursos da Petrobras, não seria possível reproduzir exatamente o comportamento do Robô ED em sua plataforma.
