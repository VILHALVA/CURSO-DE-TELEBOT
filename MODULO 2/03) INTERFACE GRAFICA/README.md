# INTERFACE GRÁFICA

## ATUALIZAÇÃO DO TELEGRAM:
Em [Abril de 2022](https://telegram.org/blog/notifications-bots/pt-br?ln=a) o Telegram lançou uma atualização que inclua ferramentas para criar interfaces infinitamente flexíveis com JavaScript. Com isso, os bots do Telegram podem substituir de forma completa qualquer site.

Essas interfaces podem ser programadas para combinar com o tema do usuário – ajustando esquemas de cores em tempo real, como acontece ao mudar entre os modos Dia e Noite ou selecionar temas [personalizados](https://telegram.org/blog/protected-content-delete-by-date-and-more/pt-br?ln=a#global-chat-themes-on-android).

Para ter uma ideia do que esperar de bots desenvolvidos por terceiros, experimente pedir fast food fictício com o nosso exemplo [@DurgerKingBot](https://t.me/DurgerKingBot).

## SOBRE O BOT:
Escreva código para responder aos comandos do bot.
Aqui está um exemplo de código para um bot simples que responde ao comando "/start":

```JavaScript
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
Use o código com cuidado. Saiba mais
Para criar um bot com uma interface infinitamente flexível, você precisará usar o componente View do SDK do Telegram Bot. O componente View permite que você crie interfaces personalizadas usando HTML, CSS e JavaScript.

Aqui está um exemplo de código para um bot com uma interface infinitamente flexível:

JavaScript
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
```

Este código criará um bot com uma interface simples que contém uma cabeçalho, um parágrafo e um botão. O botão será renderizado como um botão de texto na interface do usuário do Telegram.

Você pode personalizar a interface do seu bot usando HTML, CSS e JavaScript. Por exemplo, você pode adicionar novos elementos à interface, alterar o estilo dos elementos existentes ou adicionar interações ao bot.

**Aqui estão algumas dicas para criar um bot de Telegram com uma interface infinita:**
1. Use um framework CSS como o Bootstrap ou o Tailwind CSS para criar uma interface responsiva e elegante.

2. Use JavaScript para adicionar interações ao seu bot, como animações, efeitos e eventos.

3. Use o componentização para tornar seu código mais reutilizável e fácil de manter.

4. Teste seu bot com uma variedade de usuários para garantir que ele esteja funcionando corretamente.