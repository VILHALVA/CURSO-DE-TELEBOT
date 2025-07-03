# CONVERSADOR
## DESCRIÇÃO:
Este é um bot do Telegram que responde a mensagens de texto com respostas predefinidas, dependendo do conteúdo da mensagem. 

## EXPLICAÇÕES:
1. **Funções de Resposta:**
   - `reply_to_message(update, context)`: Esta função é chamada sempre que o bot recebe uma mensagem de texto. Ela extrai o texto da mensagem, gera uma resposta usando a função `generate_response` e envia a resposta de volta ao remetente.
   - `generate_response(message)`: Esta função gera uma resposta com base no texto da mensagem recebida. Ela verifica se a mensagem começa com determinadas palavras-chave e retorna uma resposta correspondente.

2. **Configuração do Logger:**
   - `logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)`: Isso configura o formato e o nível de logging para o programa.

3. **Criação do Updater e Dispatcher:**
   - `updater = Updater('TOKEN AQUI')`: Isso cria um objeto Updater com o token do bot fornecido.
   - `dispatcher = updater.dispatcher`: Isso cria um dispatcher que gerenciará os handlers do bot.

4. **Criação dos Handlers:**
   - `start_handler = CommandHandler('start', reply_to_message)`: Este handler responde ao comando "/start" com a função `reply_to_message`.
   - `message_handler = MessageHandler(Filters.text & (~Filters.command), reply_to_message)`: Este handler responde a todas as mensagens de texto (exceto comandos) com a função `reply_to_message`.

5. **Adição dos Handlers ao Dispatcher:**
   - Os handlers criados são adicionados ao dispatcher para que o bot possa processar os comandos e mensagens recebidos.

No geral, este código cria um bot do Telegram que responde a mensagens de texto com respostas predefinidas. Ele pode ser estendido para lidar com uma variedade de interações com o usuário.

## AVISO: OS REGISTROS NÃO SÃO PERMANENTES:
- Este bot não utiliza um banco de dados para armazenar informações dos usuários permanentemente. Em vez disso, ele salva temporariamente os dados nas variáveis durante a execução do programa. Se o bot for reiniciado ou desligado, todas as informações armazenadas serão perdidas.

- Só no `MODULO 06` do nosso curso, será possível aprender a integrar um banco de dados ao bot para armazenar as informações dos usuários permanentemente, garantindo que os dados não sejam perdidos mesmo após reinicializações ou desligamentos do bot.

