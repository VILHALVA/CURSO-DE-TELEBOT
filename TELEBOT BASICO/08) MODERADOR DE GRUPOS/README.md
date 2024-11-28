# MODERADOR DE GRUPOS
## DESCRIÇÃO:
Este é um código Python que utiliza a biblioteca Telebot para criar um bot de moderação para grupos do Telegram. Abaixo, descrevo as principais funcionalidades do código:

1. Importação de Bibliotecas:
   - O código começa importando as bibliotecas necessárias, como `telebot`, `datetime`, `re`, `os`, `pprint` e `shutil`, que são usadas para diferentes tarefas ao longo do código.

2. Configuração do Token do Bot:
   - O token do bot é definido na variável `TOKEN`. Esse token é necessário para autenticar o bot no Telegram.

3. Criação de Diretórios:
   - O código cria diretórios para armazenar informações sobre avisos e membros banidos. Os diretórios são definidos em um dicionário chamado `D`, onde as chaves são nomes de diretórios e os valores são os nomes dos diretórios reais a serem criados.

4. Controle de Avisos e Palavras Proibidas:
   - O código define um limite máximo de avisos (`MAX_AVISOS`) que um usuário pode receber antes de ser banido.
   - Uma lista de palavras proibidas (`palavras_proibidas`) é definida para detectar mensagens que contenham essas palavras.

5. Comandos e Respostas do Bot:
   - O bot responde a comandos, como `/start`, para cumprimentar os usuários quando ingressam no grupo.
   - O bot também saúda novos membros quando ingressam no grupo.

6. Função `avisar`:
   - Esta função é usada para avisar e rastrear quantos avisos um usuário recebeu. Se um usuário receber muitos avisos, ele será banido do grupo.

7. Função `palavras`:
   - Esta função verifica se uma mensagem contém palavras proibidas. Se encontrar alguma palavra proibida, a mensagem será excluída e um aviso será enviado.

8. Comando `/unban`:
   - Este comando permite aos administradores listar e desbanir membros que foram banidos anteriormente. Os membros banidos são rastreados em uma lista em memória chamada `banidos`.

9. Função `mensagens_recebidas`:
   - Esta função é chamada para todas as mensagens recebidas no grupo. Ela verifica se uma mensagem contém palavras proibidas e toma medidas, como excluir a mensagem e avisar o usuário.

10. Execução do Bot:
   - O código principal verifica se o arquivo está sendo executado diretamente (não importado como um módulo) e inicia o bot usando `bot.infinity_polling()` para mantê-lo em execução indefinidamente.

Lembre-se de que o código depende de uma configuração específica no Telegram, como administradores que podem banir membros, para funcionar corretamente. Certifique-se de que o bot tenha as permissões necessárias no grupo onde ele está sendo usado.

## DOCUMENTAÇÃO OFICIAL:
* [Atributos do objeto ChatMember](https://pytba.readthedocs.io/en/latest/types.html#telebot.types.ChatMember)

* [get_chat_member](https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.get_chat_member)

* [ban_chat_member](https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.ban_chat_member)

* [unban_chat_member](https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.unban_chat_member)