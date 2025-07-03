# CONVERSOR DE ICO: QUALQUER FOTO PARA ICO
## DESCRIÇÃO:
Este bot responderá a qualquer mensagem de foto enviada com um arquivo de ícone (.ico) convertido. Ele utiliza a biblioteca python-telegram-bot para interagir com a API do Telegram e a biblioteca Pillow para a manipulação da imagem.

## EXPLICAÇÃO:
1. **Importações de Bibliotecas:**

   * `from TOKEN import *`: Importa o token do bot armazenado em um arquivo separado `TOKEN.py`.
   * `import os`: Importa o módulo `os`, que **não está sendo utilizado** no código atual.
   * `from io import BytesIO`: Importa a classe `BytesIO`, útil para manipular arquivos em memória. **Não está sendo utilizada aqui.**
   * `from PIL import Image`: Importa a biblioteca Pillow (PIL), usada para abrir e manipular imagens.
   * `from telegram.ext import Updater, MessageHandler, Filters`: Importa os componentes principais do framework `python-telegram-bot`.

2. **Função `convert_photo_to_icon`:**

   * **Responsável por lidar com mensagens que contêm fotos e convertê-las em um arquivo `.ico` (ícone).**

3. `photo_file = update.message.photo[-1].get_file()`:

   * Acessa a versão de maior resolução da foto enviada pelo usuário.
   * Recupera o objeto de arquivo remoto do Telegram.

4. `photo_file_path = photo_file.download('input_photo.jpg')`:

   * Baixa a foto do Telegram e a salva localmente como `input_photo.jpg`.

5. `image = Image.open(photo_file_path)`:

   * Abre a imagem baixada usando Pillow.

6. **Criação dos tamanhos do ícone:**

   * `icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]`:

     * Define os tamanhos padrões que serão incluídos no arquivo `.ico` (compatíveis com múltiplas resoluções de ícones).
   * `icon_frames = []`:

     * Inicializa uma lista para armazenar as versões redimensionadas da imagem.

7. **Redimensionamento da imagem para diferentes tamanhos:**

   ```python
   for size in icon_sizes:
       resized_image = image.resize(size)
       icon_frames.append(resized_image)
   ```

   * Itera sobre cada tamanho definido em `icon_sizes`.
   * Redimensiona a imagem original para o tamanho atual.
   * Adiciona a imagem redimensionada à lista `icon_frames`.

8. **Criação do Arquivo de Ícone (.ico):**

   ```python
   output_icon_path = 'output_icon.ico'
   icon_frames[0].save(output_icon_path, icon=Image.ICO, sizes=[image.size for image in icon_frames])
   ```

   * Define o caminho de saída do arquivo `.ico`.
   * Usa o primeiro frame (`icon_frames[0]`) para iniciar o salvamento do ícone.
   * O argumento `sizes=[...]` informa ao Pillow quais tamanhos incluir no arquivo `.ico`.

9. **Envio do Arquivo `.ico` ao Usuário:**

   ```python
   context.bot.send_document(chat_id=update.effective_chat.id, document=open(output_icon_path, 'rb'))
   ```

   * Abre o arquivo `.ico` recém-gerado em modo leitura binária.
   * Envia o arquivo como documento para o usuário no chat.

10. **Função `main`:**

* Responsável por iniciar o bot e configurar os handlers.

11. `updater = Updater(TOKEN, use_context=True)`:

* Cria uma instância do `Updater` com o token do bot.
* `use_context=True` ativa o sistema moderno de contextos no `python-telegram-bot`.

12. `dp = updater.dispatcher`:

* Obtém o dispatcher, que gerencia os manipuladores de mensagens.

13. `dp.add_handler(MessageHandler(Filters.photo & ~Filters.command, convert_photo_to_icon))`:

* Adiciona um handler que escuta por mensagens que contenham **fotos** e **não sejam comandos**.
* Essas mensagens serão tratadas pela função `convert_photo_to_icon`.

14. `updater.start_polling()`:

* Inicia o polling, permitindo que o bot comece a receber mensagens.

15. `updater.idle()`:

* Mantém o bot ativo até que ele seja manualmente interrompido (ex: com `Ctrl + C`).

16. **Bloco Condicional Final:**

```python
if __name__ == '__main__':
    main()
```

* Garante que a função `main()` só seja executada quando o script for executado diretamente, e não importado por outro módulo.

## INSTRUÇÃO:
Para criar um bot que converta qualquer foto recebida para o formato `ICO`, você pode usar a biblioteca python-telegram-bot em conjunto com a biblioteca Pillow para manipulação de Foto. Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py)

Certifique-se de instalar as bibliotecas necessárias antes de executar o código:

```bash
pip install python-telegram-bot Pillow
```