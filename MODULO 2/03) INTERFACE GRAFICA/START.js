// Importe o SDK do Telegram Bot
import { Bot } from "telegram-bot-api";

// Crie uma instância do bot
const bot = new Bot({
  token: "YOUR_BOT_TOKEN",
});

// Responda ao comando "/start"
bot.on("message", (message) => {
  if (message.text === "/start") {
    bot.sendMessage(message.chat.id, "Olá, meu nome é @[BOT_USERNAME]. Eu sou um bot do Telegram criado por [YOUR_NAME].");
  }
});

// Inicie o bot
bot.start();

