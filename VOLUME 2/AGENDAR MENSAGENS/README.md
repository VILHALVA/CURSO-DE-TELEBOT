# Agendador de Mensagens Telegram
## JAVASCRIPT
Este é um bot do Telegram criado em JavaScript que permite que você agende mensagens para serem enviadas em grupos. O bot utiliza a biblioteca `telegraf` e a funcionalidade `node-schedule` para agendar as mensagens. Com este bot, você pode programar mensagens para serem enviadas em momentos específicos, útil para lembretes, anúncios e outras finalidades.

### Instruções de Uso:
1. Clone este repositório para a sua máquina local:

   ```
   git clone <link-do-repositório>
   ```

2. Instale as dependências necessárias usando o npm:

   ```
   npm install
   ```

3. Crie um bot no Telegram seguindo as instruções [aqui](https://core.telegram.org/bots#botfather), e obtenha o token do bot.

4. Crie um arquivo `.env` na raiz do projeto e adicione o token do bot:

   ```
   BOT_TOKEN=seu_token_aqui
   ```

5. Execute o bot:

   ```
   node app.js
   ```

### Comandos Disponíveis:
- `/schedule <mensagem>`: Inicia o processo de agendamento. Substitua `<mensagem>` pela mensagem que você deseja agendar.

**Instruções de Agendamento:**

1. Use o comando `/schedule` para iniciar o agendamento.

2. O bot solicitará que você insira a data e hora para enviar a mensagem. Use o formato "dd/mm/yyyy hh:mm".

3. Confirme o agendamento com o comando `/confirm_schedule`.

## PYTHON:
**Agendador de Mensagens Telegram em Python**
Este é um bot do Telegram criado em Python que permite agendar mensagens para serem enviadas em grupos. O bot utiliza a biblioteca `python-telegram-bot` para interagir com a API do Telegram e a funcionalidade de agendamento do módulo `schedule` para programar as mensagens. Com este bot, você pode facilmente agendar mensagens para serem enviadas em momentos específicos, como lembretes, anúncios e outras finalidades.

### Instruções de Uso:
1. Instale a biblioteca `python-telegram-bot` e a biblioteca `schedule` usando o pip:

   ```
   pip install python-telegram-bot schedule
   ```

2. Crie um bot no Telegram seguindo as instruções [aqui](https://core.telegram.org/bots#botfather), e obtenha o token do bot.

3. Copie o código fornecido para o arquivo do seu bot, por exemplo, `bot.py`.

4. Substitua `'SEU_TOKEN_AQUI'` pelo token do seu bot obtido no passo 2.

5. Execute o bot:

   ```
   python bot.py
   ```

### Comandos Disponíveis:
- `/schedule <mensagem>`: Inicia o processo de agendamento. Substitua `<mensagem>` pela mensagem que você deseja agendar.

### Instruções de Agendamento:
1. Use o comando `/schedule` para iniciar o agendamento.

2. O bot solicitará que você insira a data e hora para enviar a mensagem. Use o formato "dd/mm/yyyy hh:mm".

3. Confirme o agendamento com o comando `/confirm_schedule`.

## Aviso Legal:
Este bot foi criado para fins educacionais e demonstrativos. Use-o com responsabilidade e de acordo com os termos de serviço do Telegram. O desenvolvedor não assume responsabilidade por qualquer uso inadequado do bot.

## Observações:
- Certifique-se de adicionar o bot ao grupo onde você deseja agendar as mensagens.

- Certifique-se de que o arquivo `.env` esteja configurado corretamente com o token do seu bot.

- Certifique-se de que o seu bot tenha permissões suficientes para enviar mensagens no grupo.

