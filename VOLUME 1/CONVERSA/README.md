# Telegram Bot - Assistente de Conversa
## ROBO ED
Este é um projeto de um bot do Telegram que funciona como um assistente de conversa, capaz de fornecer informações sobre linguagens de programação, compartilhar mensagens de emoção e interagir com o usuário sobre diversos tópicos. O bot é criado usando a linguagem Python e a biblioteca `requests` para interagir com a API do Telegram.

### Funcionalidades
1. **Informações sobre Linguagens de Programação:** O bot fornece informações sobre várias linguagens de programação, incluindo Python, JavaScript, PHP, Java, Ruby, C++, C# e outras.

2. **Mensagens de Emoção:** O bot é capaz de compartilhar mensagens relacionadas a diferentes emoções, como amor, raiva, tristeza e alegria.

3. **Conversas sobre Tópicos Específicos:** O bot pode conversar com o usuário sobre tópicos como tecnologia, ciência, filosofia e teologia, oferecendo informações e respostas relevantes.

## SAUDAÇÃO (MELHORE O CÓDIGO)
1. **Tratamento de Mensagens:**
   No seu código, você tem dois manipuladores de mensagens, um usando a função `sample_responses` e outro usando a função `handle_message`. Parece haver um pouco de redundância aqui. Geralmente, você só precisa de um manipulador de mensagens para responder aos comandos e mensagens do usuário. No seu caso, o `sample_responses` é o que você está usando para responder a mensagens. Portanto, você pode remover o trecho relacionado a `handle_message` e usar apenas o `sample_responses`.

2. **Respostas:** 
   No manipulador de mensagens `sample_responses`, você retorna as respostas como strings. No entanto, você não está enviando essas respostas de volta para o usuário. Para enviar a resposta, você precisa usar a função `bot.send_message` da biblioteca `telebot`. Por exemplo:
   
   ```python
   @bot.message_handler(func=verificar)
   def sample_responses(input_text):
       user_message = str(input_text.text).lower()  # Correção aqui
       if user_message in ("ola", "hi", "oi"):
           bot.send_message(input_text.chat.id, "Iai! Beleza? Como está?")
       # ... outras respostas ...
       else:
           bot.send_message(input_text.chat.id, "Sinto muito! Não compreendi o que você disse")
   ```

3. **Função `error`:**
   Você definiu uma função `error`, mas não está usando-a em nenhum lugar do seu código. A função `error` é geralmente usada para lidar com erros ou exceções que possam ocorrer durante a execução do bot. Você pode adicionar a função `error` como manipulador de erros no seu bot usando `bot.add_error_handler(error)`.

4. **Recomendação para a Função `verificar`:**
   No momento, sua função `verificar` sempre retorna `True`, o que significa que ela aceitará todas as mensagens. Se você deseja filtrar mensagens com base em algum critério, você pode ajustar essa função para fazer essa verificação. Por exemplo, você pode verificar se a mensagem veio de um usuário específico, se contém determinadas palavras-chave, etc.

Lembre-se de testar seu bot cuidadosamente para garantir que todas as funcionalidades estejam funcionando conforme o esperado. Se você precisar de mais assistência ou tiver outras dúvidas, fique à vontade para perguntar!

## Como Executar o Bot?
1. Certifique-se de ter o Python instalado em sua máquina.

2. Instale a biblioteca `requests` usando o seguinte comando:
   
   ```bash
   pip install requests
   ```

3. Clone este repositório:

   ```bash
   git clone https://github.com/VILHALVA/CURSO-TELEGRAM-BOT/VOLUME%201/CONVERSA
   ```

4. Acesse o diretório do projeto:

   ```bash
   cd telegram-bot-assistente
   ```

5. Abra o arquivo `bot.py` em um editor de texto ou ambiente de desenvolvimento.

6. Substitua `"TOKEN AQUI"` pelo seu token de bot real, que você obteve ao criar o bot no BotFather no Telegram.

7. Execute o bot:

   ```bash
   python bot.py
   ```

   O bot ficará ativo e pronto para receber mensagens.

## Uso do Bot
1. Inicie uma conversa com o bot no Telegram.

2. Digite comandos como `/start`, `/amor`, `/tecnologia`, `/filosofia`, etc., para interagir com o bot e receber respostas relevantes.

3. O bot também é capaz de responder a mensagens normais, desde que sejam configuradas respostas para essas mensagens na função `gerar_respostas` do arquivo `bot.py`.

