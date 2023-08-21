# BOTÃO INLINE
## JAVASCRIPT
Para criar um bot do Telegram em JavaScript que envia uma mensagem quando um usuário clica em um botão inline, podemos utilizar a biblioteca node-telegram-bot-api.

Antes de começar, é necessário criar um bot e obter o seu token de acesso. Em seguida, vamos utilizar a classe InlineKeyboardButton para criar um botão inline e a classe InlineKeyboardMarkup para colocar esse botão em uma mensagem. Quando o usuário clicar no botão, o Telegram enviará uma consulta para o nosso bot, que deve responder com a mensagem desejada.

No código acima, a função bot.onText é registrada para lidar com mensagens que correspondem ao comando /start. Quando um usuário envia esse comando, a função cria um botão inline com o texto "Clique aqui" e o callback data "button_clicked". Em seguida, essa função envia uma mensagem para o usuário com o botão inline usando a função bot.sendMessage.

A função bot.on('callback_query', ...) é registrada para lidar com consultas de botão inline. Quando o usuário clica no botão, o Telegram envia uma consulta para o nosso bot contendo o callback data do botão. A função bot.on('callback_query', ...) é executada para lidar com essa consulta, enviando uma mensagem com o texto "Você clicou no botão!" usando a função bot.sendMessage.

Por fim, iniciamos o bot usando a função bot.startPolling().

Com esse código, o usuário pode clicar no botão inline para receber a mensagem "Você clicou no botão!" do nosso bot.

## PYTHON:
Para criar um bot do Telegram em Python que envia uma mensagem quando um usuário clica em um botão inline, podemos utilizar a biblioteca python-telegram-bot.

Antes de começar, é necessário criar um bot e obter o seu token de acesso. Em seguida, vamos utilizar a classe InlineKeyboardButton para criar um botão inline e a classe InlineKeyboardMarkup para colocar esse botão em uma mensagem. Quando o usuário clicar no botão, o Telegram enviará uma consulta para o nosso bot, que deve responder com a mensagem desejada.

No código acima, a função send_inline_button cria um botão inline com o texto "Clique aqui" e o callback data "button_clicked". Em seguida, essa função envia uma mensagem para o usuário com o botão inline usando a função update.message.reply_text.

A função button_handler é registrada como um handler para consultas de botão inline usando a classe CallbackQueryHandler. Quando o usuário clica no botão, o Telegram envia uma consulta para o nosso bot contendo o callback data do botão. A função button_handler é executada para lidar com essa consulta, enviando uma mensagem com o texto "Você clicou no botão!" usando a função query.edit_message_text.

Por fim, registramos os handlers e iniciamos o bot usando as funções add_handler, start_polling e idle.

Com esse código, o usuário pode clicar no botão inline para receber a mensagem "Você clicou no botão!" do nosso bot.