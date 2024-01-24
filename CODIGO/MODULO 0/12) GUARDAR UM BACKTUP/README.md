# GUARDAR BACKTUP
## BACKTUP DO BOT:
Este é um script Python que cria um bot de Telegram que pode fazer o backup dos arquivos do bot e enviá-los para o Telegram quando um comando é acionado. Aqui está uma descrição do que cada parte do código faz:

1. Importação de Módulos:
   - `telebot`: Importa a biblioteca Telebot, que permite criar um bot do Telegram e interagir com ele.
   - `shutil`: Importa a biblioteca Shutil, usada para criar um arquivo ZIP dos arquivos do bot.
   - `os`: Importa a biblioteca OS, que fornece funcionalidades para interagir com o sistema operacional, como manipulação de arquivos e diretórios.

2. Definição de Token e Administradores:
   - `TOKEN`: Define o token do bot do Telegram. Substitua-o pelo token do seu próprio bot.
   - `ADMINS`: Define o ID do administrador (você pode adicionar mais IDs separados por vírgulas). Apenas os administradores podem acionar comandos de backup.

3. Criação do Bot:
   - `bot = telebot.TeleBot(TOKEN)`: Cria uma instância do bot usando o token fornecido.

4. Comando `/start`:
   - Quando um usuário digita `/start`, o bot responde com uma mensagem de boas-vindas formatada em HTML.

5. Função `es_admin`:
   - Verifica se o ID do usuário que enviou a mensagem é um administrador autorizado.
   - Se o ID estiver na lista de administradores, retorna `True`; caso contrário, retorna `False`.

6. Comando `/backtup`:
   - Quando um administrador digita `/backtup`, o bot realiza as seguintes ações:
     - Determina o diretório do script atual.
     - Define o caminho do arquivo ZIP que será criado (usando o diretório do script e voltando um nível).
     - Cria um arquivo ZIP contendo os arquivos do diretório do script (exceto o próprio arquivo ZIP).
     - Envia o arquivo ZIP para o chat atual do Telegram.
     - Remove o arquivo ZIP do sistema de arquivos.

7. Execução Principal:
   - O código verifica se o script está sendo executado diretamente (não importado como um módulo).
   - Se for o caso, inicia o bot e o mantém em execução com `bot.infinity_polling`.

Lembre-se de substituir o valor de `TOKEN` pelo token real do seu bot e adicione os IDs de administradores apropriados em `ADMINS`. Certifique-se de que o bot tenha permissões para enviar documentos no chat em que ele opera.

## DIRETORIOS:
Este é um código Python que utiliza a biblioteca `telebot` para criar um bot do Telegram que pode ser usado para fazer backup dos arquivos em um diretório específico. Aqui está uma descrição das principais partes do código:

1. Importação de Bibliotecas:
   - O código começa importando as bibliotecas necessárias, incluindo `telebot` para criar e controlar o bot do Telegram, `zipfile` para criar arquivos ZIP, `tempfile` para trabalhar com arquivos temporários e `os` para operações no sistema de arquivos.

2. Definição das Variáveis:
   - `TOKEN`: Esta variável armazena o token do seu bot Telegram. Você deve substituí-la pelo token do seu próprio bot.
   - `ADMINS`: Esta variável armazena o ID de administrador. É usado para verificar se o usuário que interage com o bot é um administrador autorizado.
   - `bot`: É uma instância da classe `TeleBot` que representa o bot Telegram e é inicializada com o token fornecido.

3. Comando `/start`:
   - A função `cmd_start` é um manipulador de mensagens para o comando `/start`. Quando um usuário envia este comando, o bot responde com uma mensagem de boas-vindas.

4. Função `es_admin`:
   - Esta função verifica se o ID do chat (`cid`) é igual ao ID do administrador (`ADMINS`). Se for, retorna `True`, caso contrário, envia uma mensagem de erro e retorna `False`.

5. Função `zipdir`:
   - Esta função cria um arquivo ZIP contendo os arquivos de um diretório específico. Os parâmetros incluem o nome do arquivo ZIP, o diretório a ser compactado e uma lista de arquivos a serem excluídos do backup. A função retorna o caminho do arquivo ZIP criado.

6. Comando `/backtup`:
   - A função `cmd_backtup` é um manipulador de mensagens para o comando `/backtup`. Esta função só será executada se o ID do chat for igual ao ID de administrador. Ela cria um arquivo ZIP chamado "mi_bot.zip" que contém os arquivos do diretório atual, excluindo aqueles listados na variável `excluir`. Em seguida, envia o arquivo ZIP como um documento para o chat e o remove do sistema de arquivos temporários.

7. Fluxo Principal:
   - O código principal verifica se o script está sendo executado diretamente (`if __name__ == '__main__'`). Se for o caso, inicia o bot com `bot.infinity_polling(timeout=60)` e exibe uma mensagem indicando que o bot foi iniciado.

Lembre-se de substituir o token do bot e o ID do administrador pelo seu próprio token e ID. Certifique-se também de que a biblioteca `telebot` esteja instalada no ambiente em que você está executando o código. Este bot responde ao comando `/start` com uma mensagem de boas-vindas e, se o usuário for um administrador autorizado, responde ao comando `/backtup` com um arquivo ZIP contendo os arquivos do diretório atual.

## DOCUMENTAÇÃO:
[os.path.join()](https://docs.python.org/es/3/library/os.path.html#os.path.join)

[tempfile.gettempdir()](https://docs.python.org/es/3/library/tempfile.html#tempfile.gettempdir)

[zipfile](https://docs.python.org/es/3/library/zipfile.html)
