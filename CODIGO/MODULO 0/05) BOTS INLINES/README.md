# BOTS INLINES
## CRIANDO O BOT:
Para criar um bot inline no BotFather e torná-lo capaz de responder a consultas em qualquer chat, você precisa seguir os seguintes passos:

1. **Crie um novo bot no BotFather:**

   Abra o Telegram e procure por "BotFather". Inicie uma conversa com o BotFather e siga estas etapas:

   - Use o comando `/newbot` para criar um novo bot.
   - Dê um nome ao seu bot.
   - Escolha um nome de usuário para o seu bot. Ele deve terminar com a palavra "bot" e ser único no Telegram. Por exemplo, "meu_bot_telegram_bot".
   - O BotFather fornecerá um token de acesso único para o seu bot. Anote esse token, pois você precisará dele para autenticar seu bot.

2. **Habilitar modo inline:**

   Para tornar seu bot capaz de responder a consultas em qualquer chat, você precisa habilitar o modo inline. Para fazer isso, siga estas etapas:

   - Abra uma conversa privada com o BotFather novamente.
   - Use o comando `/mybots` para listar seus bots.
   - Selecione o bot que você criou anteriormente.
   - Selecione a opção `Bot Settings`.
   - Selecione a opção `Inline Mode`.
   - Ative o modo inline.

3. **Configurar respostas inline:**

   Agora que você ativou o modo inline, você pode configurar como o seu bot responderá a consultas em qualquer chat. Para fazer isso, você precisa definir respostas inline para diferentes consultas.

   - Para configurar respostas inline, você precisa usar a API do Telegram para o seu bot. Você pode programar o comportamento do seu bot para responder a consultas inline com base em palavras-chave, consultas de pesquisa etc.

   - Certifique-se de que o seu bot esteja funcionando com um servidor onde você possa implementar lógica para tratar essas consultas inline.

4. **Implantar seu bot:**

   Você precisará hospedar seu bot em algum lugar (por exemplo, um servidor web) para que ele possa responder a consultas inline. O bot precisa estar sempre ativo para responder a consultas.

5. **Definir resultados inline:**

   Quando você recebe uma consulta inline, você deve usar a API do Telegram para enviar resultados inline para o usuário. Cada resultado inline deve incluir um título, uma descrição e um URL (opcional).

6. **Ativar o bot inline:**

   Agora, seu bot estará pronto para responder a consultas inline em qualquer chat no Telegram. Os usuários podem mencionar seu bot em qualquer chat público e começar a usá-lo.

Lembre-se de que responder a consultas inline requer programação personalizada e hospedagem do bot, já que você precisa implementar a lógica para processar as consultas e retornar resultados relevantes. 

## EXEMPLO INLINE:
**Descrição:**
Este é um exemplo de um bot Telegram que demonstra o uso do modo inline. O bot responde a consultas inline com resultados diferentes, dependendo das palavras-chave usadas pelo usuário.

**Funcionalidades:**
1. **Consultas de Texto:** Quando um usuário envia a palavra-chave "text", o bot responde com dois resultados de artigos inline, cada um com um título e uma mensagem de texto.

2. **Consultas de Foto:** Se o usuário enviar a palavra-chave "photo1", o bot responderá com dois resultados de fotos inline, cada um com uma imagem de gato e uma mensagem de texto.

3. **Consultas de Vídeo:** Quando o usuário envia a palavra-chave "video", o bot responde com um resultado de vídeo inline, exibindo um vídeo de demonstração e uma mensagem de título.

4. **Consulta Padrão:** Se o usuário não especificar nenhuma palavra-chave, o bot responderá com um resultado de artigo inline padrão com uma mensagem de texto.

**Funcionamento:**
O bot utiliza a biblioteca `pyTelegramBotAPI` para interagir com a API do Telegram. Ele está configurado para responder a consultas inline específicas com resultados predefinidos.

**Observações:**
- O bot requer um token de API do Telegram para funcionar, que deve ser configurado no código.
- O bot foi projetado para fins de demonstração e pode ser personalizado ou expandido para atender a diferentes necessidades.

Este bot de demonstração é útil para entender como os bots inline funcionam no Telegram e pode ser um ponto de partida para o desenvolvimento de bots mais complexos que respondem a consultas inline de maneira personalizada.