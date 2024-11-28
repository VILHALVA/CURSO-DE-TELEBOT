# COMANDOS VIA BARRA (/)
## CADA BOT TEM SEUS COMANDOS:
Este é um exemplo de código em Python que demonstra como criar um bot do Telegram que fornece informações sobre qualquer assunto. O bot responde aos comandos `/[NOME DO COMANDO]`.

## EXPLICAÇÃO:
O código faz parte de um bot do Telegram em Python e é utilizado para criar comandos específicos e respostas para mensagens recebidas pelo bot. Vamos dividir a explicação em duas partes:

1. **Handler para o comando "/sol":**
   ```python
   @bot.message_handler(commands=["sol"])
   def sol(mensagem):
       bot.send_message(mensagem.chat.id, "TEXTO_AQUI")
   ```
   - Este código cria um handler para mensagens que começam com o comando "/sol".
   - Quando o bot recebe uma mensagem contendo "/sol", ele executa a função `sol`.
   - A função `sol` envia uma mensagem de volta para o chat de onde veio a mensagem original, com o texto "TEXTO_AQUI" substituído pelo conteúdo real que você deseja enviar.

2. **Handler para os comandos "/start" e "/menu" com uma função personalizada:**
   ```python
   @bot.message_handler(func=verificar, commands=["start", "menu"])
   def responder(mensagem):
       texto = '''
       🛑ESCOLHA UMA DAS OPÇÕES:
       /sol > A estrela do tipo G
       /mercurio > O mensageiro
       /venus > Deusa do amor
       /terra > Deusa Gaia
       /marte > Deus da guerra
       /jupiter > O Zeus
       /saturno > O Cronos
       /urano > Pai de Cronos
       /netuno > Deus Poseidon
       💚RESPONDER QUALQUER MENSAGEM NÃO IRÁ FUNCIONAR!!'''
       bot.reply_to(mensagem, texto)
   ```
   - Este código cria um handler para mensagens que começam com os comandos "/start" ou "/menu".
   - Ele utiliza uma função personalizada `verificar` (que não está explicitamente definida no trecho de código fornecido). Essa função deve retornar True ou False para determinar se o handler deve ser acionado ou não. Presumivelmente, ela verifica se a mensagem atende a algum critério específico.
   - Quando o bot recebe uma mensagem contendo "/start" ou "/menu" e a função `verificar` retorna True, ele executa a função `responder`.
   - A função `responder` envia uma mensagem de volta para o chat de onde veio a mensagem original, com um texto que lista várias opções de comandos disponíveis para o usuário.
