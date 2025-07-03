# DOCUMENTOS PARA PDF
## DESCRIÇÃO:
Este bot responderá a qualquer mensagem de documento enviada com um arquivo de documento PDF convertido. Ele utiliza a biblioteca python-telegram-bot para interagir com a API do Telegram e o libreoffice para a conversão de documentos em PDF.

## EXPLICAÇÃO:
1. **Importações:**

   * `from TOKEN import *`: Importa o token do bot a partir do arquivo `TOKEN.py`.
   * `import os`: Importa o módulo `os`, usado para executar comandos no sistema operacional (neste caso, o `libreoffice`).
   * `from telegram.ext import Updater, MessageHandler, Filters`: Importa as ferramentas da biblioteca `python-telegram-bot` para criação do bot:

     * `Updater`: gerencia a conexão com a API do Telegram.
     * `MessageHandler`: escuta tipos específicos de mensagens (aqui, documentos).
     * `Filters`: permite filtrar mensagens com base no conteúdo (ex: `document`, `command`).

2. **Função `convert_document_to_pdf`:**

   * Responsável por lidar com documentos enviados ao bot e convertê-los para o formato PDF.

3. `document_file = update.message.document.get_file()`:

   * Acessa o arquivo de documento anexado à mensagem enviada pelo usuário.

4. `document_file_path = document_file.download('input_document')`:

   * Baixa o documento enviado e salva localmente com o nome `input_document` (sem extensão).

5. **Comando de Conversão com LibreOffice:**

```python
os.system(f'libreoffice --headless --convert-to pdf --outdir . {document_file_path}')
```

* Usa o LibreOffice no modo *headless* (sem interface gráfica) para converter o documento para PDF.
* `--convert-to pdf`: define o formato de saída como PDF.
* `--outdir .`: define o diretório de saída como o diretório atual.
* `{document_file_path}`: o caminho do arquivo a ser convertido.
* **Resultado:** será criado um arquivo com mesmo nome base, mas com extensão `.pdf` no mesmo diretório.

> ⚠️ **Importante:** o LibreOffice deve estar instalado no sistema e disponível no `PATH`.

6. `output_pdf_path = 'output_document.pdf'`:

   * Define o nome do arquivo PDF a ser enviado.
   * **Observação:** esse nome **precisa corresponder ao nome gerado pelo LibreOffice**. Se o arquivo original tiver outro nome, isso pode causar erro. Aqui o nome está hardcoded como `output_document.pdf`, o que exige que o arquivo enviado também se chame `input_document` e tenha uma extensão compatível (ex: `.docx`, `.odt`, etc.).

7. `context.bot.send_document(chat_id=update.effective_chat.id, document=open(output_pdf_path, 'rb'))`:

   * Envia o arquivo PDF convertido de volta ao usuário.

8. **Função `main`:**

   * Responsável por iniciar o bot e registrar os handlers.

9. `updater = Updater(TOKEN, use_context=True)`:

   * Cria a instância do `Updater` com o token do bot.

10. `dp = updater.dispatcher`:

* Obtém o dispatcher, que gerencia os handlers registrados.

11. `dp.add_handler(MessageHandler(Filters.document & ~Filters.command, convert_document_to_pdf))`:

* Registra um handler que será acionado sempre que o bot receber uma **mensagem com um documento**, desde que **não seja um comando**.

12. `updater.start_polling()`:

* Inicia o processo de verificação contínua por novas mensagens no Telegram.

13. `updater.idle()`:

* Mantém o bot em execução até que seja interrompido manualmente.

14. **Bloco principal:**

```python
if __name__ == '__main__':
    main()
```

* Garante que a função `main()` será executada apenas quando o script for rodado diretamente (e não importado como módulo).

## INSTRUÇÃO:
Para criar um bot que converte documentos em vários formatos para PDF, você pode usar a biblioteca python-telegram-bot e o libreoffice para a conversão. Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py)

Certifique-se de instalar as bibliotecas necessárias antes de executar o código:

```bash
pip install libreoffice
```