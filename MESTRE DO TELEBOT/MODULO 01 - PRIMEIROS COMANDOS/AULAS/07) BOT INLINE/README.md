# EXEMPLO DE BOT INLINE
## DESCRIÇÃO:
Este bot é um exemplo básico de um bot de modo inline que responde a consultas dos usuários com resultados de artigo, foto e vídeo.

## EXPLICAÇÃO:
1. **`query_text`**: Esta função trata consultas que contêm o texto 'text'. Ele cria dois resultados de consulta inline do tipo `InlineQueryResultArticle`, que exibem simplesmente a mensagem 'hi'.

2. **`query_photo`**: Esta função trata consultas que contêm o texto 'photo1'. Ela cria dois resultados de consulta inline do tipo `InlineQueryResultPhoto`, cada um com uma imagem de gatinho e um galo, respectivamente.

3. **`query_video`**: Esta função trata consultas que contêm o texto 'video'. Ela cria um resultado de consulta inline do tipo `InlineQueryResultVideo`, que mostra um vídeo. Além disso, há um título associado ao vídeo.

4. **`default_query`**: Esta função lida com consultas em branco ou vazias, fornecendo uma resposta padrão.

5. **`main_loop`**: Esta função inicia o bot e entra em um loop infinito de polling para receber atualizações.

6. **Tratamento de Exceções**: Cada função de tratamento de consulta (query handler) está envolvida em um bloco `try-except` para lidar com exceções que possam ocorrer durante a execução.

## COMO CONFIGURAR?
Para configurar seu bot para ser inline no BotFather, siga estas etapas:

1. Abra o Telegram e inicie uma conversa com o [BotFather.](https://t.me/BotFather)

2. Uma vez na conversa com o BotFather, use o comando "/start" para iniciar a interação ou apenas digite "/newbot" para criar um novo bot, se ainda não tiver feito isso.

3. Siga as instruções do BotFather para criar seu novo bot, fornecendo um nome e um username para o seu bot.

4. Após criar o bot, o BotFather fornecerá um token de acesso único para o seu bot. Guarde este token com segurança, pois você precisará dele para configurar seu bot inline.

5. Para habilitar a funcionalidade inline para o seu bot, use o comando "/setinline" na conversa com o BotFather.

6. O BotFather pedirá que você forneça uma descrição para a funcionalidade inline do seu bot. Digite uma descrição breve e informativa que descreva o propósito do bot inline.

7. Após configurar a funcionalidade inline, você pode definir algumas configurações adicionais, como a sugestão de botões para resultados inline e a capacidade de editar mensagens. Siga as instruções do BotFather para configurar essas opções conforme desejado.

8. Depois de configurar todas as opções desejadas, seu bot estará configurado para funcionar inline.


