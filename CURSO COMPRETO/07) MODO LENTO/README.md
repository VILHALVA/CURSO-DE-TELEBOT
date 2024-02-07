# MODO LENTO
Este é um bot de exemplo escrito em Python usando a biblioteca `telebot` para Telegram. Aqui está uma descrição do que ele faz:

1. Quando você envia o comando `/start` para o bot, ele responde com a mensagem "BOT INICIADO..." formatada em HTML.

2. O bot possui um sistema de modo lento incorporado. Isso significa que, se alguém enviar uma mensagem em um intervalo menor do que um determinado limite de tempo (definido como `MODO_LENTO`), o bot responderá com uma mensagem informando que o usuário deve esperar antes de enviar outra mensagem.

3. O bot mantém o controle do tempo da última mensagem de cada usuário em um arquivo separado no diretório `modo_lento`. Se um usuário envia mensagens em intervalos muito curtos, o bot irá detectar isso e pedir que o usuário espere o tempo definido no modo lento antes de enviar outra mensagem.

4. O bot exclui automaticamente a mensagem que o usuário enviou se ela foi enviada antes do tempo necessário no modo lento.

5. Para outras mensagens que não acionam o modo lento, o bot simplesmente responde com a mensagem "PROCESSANDO..." formatada em HTML.

Lembre-se de substituir o valor de `TOKEN` pelo token real do seu bot para que ele funcione corretamente. Este código pode ser usado como base para criar bots com recursos de moderação, como controle de spam ou restrições de frequência de mensagens.