## DOWNLOAD DE IMAGENS
Este é um exemplo de um bot do Telegram que permite aos usuários enviar uma descrição de uma imagem ou uma palavra-chave e, em resposta, o bot envia uma imagem relacionada usando a API do Pexels. O bot foi implementado em Python e JavaScript.

### Requisitos
- [Python](https://www.python.org/) (para a versão em Python)
- [Node.js](https://nodejs.org/) (para a versão em JavaScript)
- [Telegram Bot Token](https://core.telegram.org/bots#botfather) (obtenha isso criando um novo bot no Telegram)
- [Chave de Acesso à API do Pexels](https://www.pexels.com/api/) (crie uma conta no Pexels e obtenha a chave)

### Versão Python
1. Instale as bibliotecas necessárias:

```bash
pip install python-telegram-bot requests
```

2. Substitua `SEU_TOKEN` pelo token do seu bot e `SUA_CHAVE_DO_PEXELS` pela sua chave de acesso à API do Pexels no arquivo `bot_python.py`.

3. Execute o bot em Python:

```bash
python bot_python.py
```

O bot responderá às mensagens dos usuários com uma imagem correspondente à descrição ou palavra-chave fornecida, usando a API do Pexels.

### Versão JavaScript
1. Instale as bibliotecas necessárias:

```bash
npm install node-telegram-bot-api axios
```

2. Substitua `SEU_TOKEN` pelo token do seu bot e `SUA_CHAVE_DO_PEXELS` pela sua chave de acesso à API do Pexels no arquivo `bot_javascript.js`.

3. Execute o bot em JavaScript:

```bash
node bot_javascript.js
```

O bot responderá às mensagens dos usuários com uma imagem correspondente à descrição ou palavra-chave fornecida, usando a API do Pexels.

### Como Usar
1. Inicie uma conversa com o bot no Telegram.

2. Envie uma descrição de uma imagem ou uma palavra-chave.

3. O bot responderá com uma imagem relacionada à descrição ou palavra-chave fornecida, usando a API do Pexels.

Lembre-se de respeitar os termos de uso da API do Pexels e considere a privacidade dos usuários ao lidar com imagens. Certifique-se também de que o bot esteja funcionando corretamente e de que as credenciais estejam configuradas adequadamente.