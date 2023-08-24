// Importe o SDK do Telegram Bot
import { Bot, View } from "telegram-bot-api";

// Crie uma instância do bot
const bot = new Bot({
  token: "YOUR_BOT_TOKEN",
});

// Crie uma interface
const view = new View({
  template: `
    <div class="container">
      <h1>Meu bot do Telegram</h1>
      <p>Este é um bot do Telegram com uma interface infinita.</p>
      <button id="button">Clique aqui</button>
    </div>
  `,
});

// Responda ao comando "/start"
bot.on("message", (message) => {
  if (message.text === "/start") {
    bot.sendMessage(message.chat.id, "Olá, meu nome é @[BOT_USERNAME]. Eu sou um bot do Telegram criado por [YOUR_NAME].");
    bot.sendMessage(message.chat.id, view.render());
  }
});

// Inicie o bot
bot.start();
