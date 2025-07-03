# CONVERSOR DE FOTO: QUALQUER FOTO PARA PNG
## DESCRIÇÃO:
Este bot responderá a qualquer mensagem de foto enviada com uma imagem PNG convertida. Ele utiliza a biblioteca python-telegram-bot para interagir com a API do Telegram e a biblioteca Pillow para a manipulação da imagem.

## EXPLICAÇÃO:
1. **Importação de Dependências:**

   * `from TOKEN import *`: Importa o token de autenticação do bot armazenado em um arquivo separado `TOKEN.py`.
   * `import os`: Importa o módulo `os`, embora **não esteja sendo utilizado nesse código** (poderia ser removido).
   * `from io import BytesIO`: Importa `BytesIO` da biblioteca `io`, que serve para manipular dados binários em memória. **Não está sendo usado no código atual**.
   * `from PIL import Image`: Importa a biblioteca PIL (via Pillow), usada para abrir e salvar imagens.
   * `from telegram.ext import Updater, MessageHandler, Filters`: Importa os componentes principais do framework `python-telegram-bot`.

2. **Função `convert_photo_to_png`:**

   * **Responsável por tratar mensagens que contenham fotos.**

3. `photo_file = update.message.photo[-1].get_file()`:

   * Acessa a **última versão** da foto (maior resolução).
   * Recupera o objeto `File` correspondente, que pode ser baixado.

4. `photo_file_path = photo_file.download('input_photo.jpg')`:

   * Baixa a imagem do Telegram e a salva no disco com o nome `input_photo.jpg`.

5. `image = Image.open(photo_file_path)`:

   * Abre a imagem salva usando a biblioteca Pillow (PIL) para manipulá-la.

6. `image.save('output_photo.png', 'PNG')`:

   * Converte a imagem para o formato PNG e a salva como `output_photo.png`.

7. `context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('output_photo.png', 'rb'))`:

   * Envia a imagem convertida de volta ao usuário.
   * Usa `open(..., 'rb')` para abrir o arquivo em modo de leitura binária.

8. **Função `main`:**

   * Responsável por inicializar o bot e registrar os manipuladores de mensagens.

9. `updater = Updater(TOKEN, use_context=True)`:

   * Cria o objeto `Updater` com o token do bot.
   * `use_context=True` ativa o novo sistema baseado em `context`, recomendado nas versões mais recentes da biblioteca.

10. `dp = updater.dispatcher`:

    * Recupera o dispatcher do updater, que será usado para adicionar os handlers.

11. `dp.add_handler(MessageHandler(Filters.photo & ~Filters.command, convert_photo_to_png))`:

    * Adiciona um `MessageHandler` que reage a mensagens que contenham **fotos** e **não sejam comandos**.
    * Vincula essas mensagens à função `convert_photo_to_png`.

12. `updater.start_polling()`:

    * Inicia o polling para receber atualizações do Telegram em tempo real.

13. `updater.idle()`:

    * Mantém o bot em execução até que seja encerrado manualmente (como com `Ctrl + C`).

14. **Bloco Condicional `if __name__ == '__main__':`**:

    * Garante que a função `main()` só seja executada quando o script for executado diretamente (e não importado por outro módulo).

## INSTRUÇÃO:
Para criar um bot que converta qualquer foto recebida para o formato PNG, você pode usar a biblioteca python-telegram-bot em conjunto com a biblioteca Pillow para manipulação de Foto. Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py)

Certifique-se de instalar as bibliotecas necessárias antes de executar o código:

```bash
pip install python-telegram-bot Pillow
```