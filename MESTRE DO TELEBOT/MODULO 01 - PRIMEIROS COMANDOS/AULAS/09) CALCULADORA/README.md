# BOT DE CALCULADORA
## DESCRIÇÃO:
O Bot de Calculadora é uma aplicação desenvolvida para o Telegram que permite aos usuários realizarem operações matemáticas simples diretamente na conversa com o bot, de maneira prática e rápida.

## FUNCIONALIDADES:
1. **Inicia a interação**: Ao iniciar uma conversa com o bot, o usuário recebe uma mensagem de boas-vindas.

2. **Fornece ajuda**: Com o comando `/ajuda`, o usuário recebe uma lista de comandos disponíveis e instruções de uso.

3. **Realiza cálculos matemáticos**: O bot suporta os seguintes comandos matemáticos:

   * `/somar valor1 valor2`: Calcula a soma de dois números.
   * `/subtrair valor1 valor2`: Calcula a subtração entre dois números.
   * `/multiplicar valor1 valor2`: Calcula a multiplicação de dois números.
   * `/dividir valor1 valor2`: Calcula a divisão entre dois números (com verificação de divisão por zero).

4. **Responde com o resultado**: Após o envio de um comando válido, o bot responde com o resultado do cálculo.

5. **Lida com entradas inválidas**: Se o usuário enviar comandos com argumentos incorretos ou mensagens desconhecidas, o bot responde informando que não entendeu.

## EXPLICAÇÃO:
### **CONFIG.py**:
* Contém a configuração do bot:

  * Importa a biblioteca `telebot`.
  * Define o token fornecido pelo BotFather.
  * Cria o objeto `bot` com o token.

### **MAIN.py**:
1. **Importações:**

* Importa `bot` de `CONFIG`, `sleep` da biblioteca `time` e outras bibliotecas padrão.

2. **Comandos do Bot:**

* `@bot.message_handler(commands=['start'])`: Exibe uma mensagem de boas-vindas ao iniciar a conversa.
* `@bot.message_handler(commands=['ajuda'])`: Exibe a lista de comandos e como utilizá-los.

3. **Comandos matemáticos via barra:**

* `@bot.message_handler(commands=['somar'])`: Extrai dois valores e retorna a soma.
* `@bot.message_handler(commands=['subtrair'])`: Extrai dois valores e retorna a subtração.
* `@bot.message_handler(commands=['multiplicar'])`: Extrai dois valores e retorna a multiplicação.
* `@bot.message_handler(commands=['dividir'])`: Extrai dois valores e retorna a divisão (com verificação para divisão por zero).

> Todos os comandos esperam exatamente dois argumentos numéricos após a barra. Se os valores forem inválidos ou estiverem ausentes, o bot informa como usar corretamente.

4. **Função auxiliar `obter_valores_argumentos`:**

* Analisa a mensagem do usuário, divide os argumentos e tenta converter os valores para `float`.

5. **Tratamento de mensagens inválidas:**

* `@bot.message_handler(func=lambda message: True)`: Captura mensagens que não correspondem a nenhum comando e envia uma resposta de erro amigável.

6. **Execução do bot:**

* O bot é executado com `bot.polling(timeout=20)`.

## COMO USAR?
1. **Coloque o Token:**
   - Antes de executar o bot, é necessário substituir o token do seu bot no arquivo `./CODIGO/CONFIG.py`, o qual pode ser obtido por meio do [@BotFather](https://t.me/BotFather).

2. **Inicie o Bot:**
   - Execute o bot do Telegram em Python iniciando-o com o seguinte comando:
   ```bash
   python MAIN.py
   ```

3. Abra o Telegram e inicie uma conversa com o bot. Para isso, pesquise pelo nome de usuário do bot.

4. Utilize os seguintes comandos diretamente na conversa:

   * `/start`: Inicia a interação com o bot e exibe uma saudação inicial.
   * `/ajuda`: Mostra uma mensagem com instruções e comandos disponíveis.
   * `/somar valor1 valor2`: Soma dois valores.
     Exemplo: `/somar 5 3`
   * `/subtrair valor1 valor2`: Subtrai o segundo valor do primeiro.
     Exemplo: `/subtrair 10 4`
   * `/multiplicar valor1 valor2`: Multiplica dois valores.
     Exemplo: `/multiplicar 6 7`
   * `/dividir valor1 valor2`: Divide o primeiro valor pelo segundo.
     Exemplo: `/dividir 20 4`

5. O bot responderá com o resultado da operação ou avisará caso o comando esteja incorreto.

