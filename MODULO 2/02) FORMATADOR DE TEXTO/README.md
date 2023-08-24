# FORMATADOR DE TEXTO
O FormatBot é um bot do Telegram que permite aos usuários formatar o texto de maneiras criativas usando comandos específicos. Ele suporta várias formatações, como negrito, itálico, código, links, emojis de bandeiras e muito mais. Você pode usar o bot para aplicar essas formatações ao texto que você envia.

## Como Usar
### Versão Python
1. **Obtenha o Token do Bot:** Primeiro, você precisará criar um bot no Telegram usando o BotFather e obter o token de acesso.

2. **Instale as Dependências:** Certifique-se de ter o módulo `requests` instalado. Caso contrário, instale usando o seguinte comando:

   ```
   pip install requests
   ```

3. **Configure o Token:** Substitua `"SEU_TOKEN_AQUI"` pelo token do seu bot na variável `TOKEN` no código.

4. **Execute o Bot:** Execute o script Python. O bot estará pronto para receber mensagens e responder com o texto formatado.

### Versão JavaScript
1. **Obtenha o Token do Bot:** Assim como na versão Python, você precisa criar um bot no Telegram usando o BotFather e obter o token de acesso.

2. **Instale as Dependências:** Certifique-se de ter a biblioteca `node-telegram-bot-api` instalada. Caso contrário, instale usando o seguinte comando:

   ```
   npm install node-telegram-bot-api
   ```

3. **Configure o Token:** Substitua `'SEU_TOKEN_AQUI'` pelo token do seu bot no código.

4. **Execute o Bot:** Execute o script JavaScript. O bot estará pronto para receber mensagens e responder com o texto formatado.

## Comandos Disponíveis
- `/start`: Inicia a conversa com o bot e exibe as instruções de formatação disponíveis.

## Formatações Suportadas
O bot suporta as seguintes formatações:

- `*grassetto*`: **grassetto**
- `_corsivo_`: _corsivo_
- \`code\`: `code`
- `[Google](https://www.google.com)`: [Google](https://www.google.com/)
- `%blu%`: 🇧 🇱 🇺
- `-barrato-`: ~~barrato~~
- `;sottolineato;`: s̲o̲t̲t̲o̲l̲i̲n̲e̲a̲t̲o
- `^grande^`: ｇｒａｎｄｅ
- `&maiuscoletto&`: ᴍᴀɪᴜsᴄᴏʟᴇᴛᴛᴏ
- `@bolle@`: ⒷⓄⓁⓁⒺ

## Aviso
Este bot foi criado apenas para fins educacionais e de demonstração. Certifique-se de seguir as diretrizes do Telegram ao criar e usar bots.

**Nota:** O bot não possui capacidade de armazenamento de mensagens, portanto, não manterá um registro das mensagens enviadas.

Sinta-se à vontade para usar, modificar e aprimorar o código do bot de acordo com suas necessidades. Divirta-se formatando o texto!