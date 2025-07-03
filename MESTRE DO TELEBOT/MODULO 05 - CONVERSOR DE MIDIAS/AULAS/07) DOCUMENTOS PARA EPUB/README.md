# DOCUMENTOS PARA EPUB
## DESCRIÇÃO:
Este bot responderá a qualquer mensagem de documento enviada com um arquivo de documento EPUB convertido. Ele utiliza a biblioteca python-telegram-bot para interagir com a API do Telegram e a biblioteca ebooklib para a conversão de documentos em EPUB.

## EXPLICAÇÃO:
1. **Importações:**

```python
from TOKEN import *
```

* Importa a variável `TOKEN` (com o token de autenticação do bot Telegram) a partir de um arquivo externo chamado `TOKEN.py`.

```python
import os
```

* Importa o módulo `os`, utilizado aqui para manipulação de arquivos (embora não esteja diretamente usado no script atual).

```python
from telegram.ext import Updater, MessageHandler, Filters
```

* Importa os componentes da biblioteca `python-telegram-bot`:

  * `Updater`: responsável por conectar o bot à API do Telegram.
  * `MessageHandler`: escuta e trata mensagens recebidas.
  * `Filters`: define os tipos de mensagens que ativam os handlers (ex: documentos).

```python
from ebooklib import epub
```

* Importa a biblioteca `ebooklib`, usada para criar e manipular arquivos `.epub`.

2. **Função `convert_document_to_epub`**:

Responsável por converter qualquer documento enviado pelo usuário para o formato EPUB.

```python
document_file = update.message.document.get_file()
```

* Obtém o objeto do arquivo do documento enviado pelo usuário.

```python
document_file_path = document_file.download('input_document')
```

* Faz o download do arquivo recebido e o salva localmente com o nome `input_document`.

3. **Criação do arquivo EPUB:**

```python
output_epub_path = 'output_document.epub'
book = epub.EpubBook()
```

* Define o nome do arquivo EPUB a ser salvo e cria um novo objeto do tipo `EpubBook`.

4. **Configuração dos metadados do livro:**

```python
book.set_identifier('document_conversion')
book.set_title('Converted Document')
book.set_language('en')
```

* Define um identificador único, título e idioma do livro EPUB.

5. **Leitura do conteúdo do documento original:**

```python
with open(document_file_path, 'rb') as f:
    contents = f.read()
```

* Abre o arquivo baixado em modo binário e lê seu conteúdo.

6. **Criação de um capítulo para o EPUB:**

```python
chapter = epub.EpubHtml(title='Converted Document', file_name='document.xhtml', lang='en')
chapter.content = contents
```

* Cria um capítulo HTML no EPUB com o conteúdo bruto do arquivo lido.

> ⚠️ **Atenção:** Se o arquivo não estiver em HTML ou texto formatado (ex: `.docx`, `.odt`, etc.), isso pode causar problemas no EPUB.

7. **Adição do capítulo ao livro:**

```python
book.add_item(chapter)
book.toc = (epub.Link('document.xhtml', 'Converted Document', 'converted_document'), )
```

* Adiciona o capítulo ao livro e o inclui na Tabela de Conteúdo (TOC).

8. **Adição de itens obrigatórios para navegação:**

```python
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
```

* Adiciona os arquivos de navegação padrão exigidos pelo formato EPUB (`NCX` e `Nav`).

9. **Estilização do EPUB:**

```python
style = 'body { font-family: Times, Times New Roman, serif; }'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
book.add_item(nav_css)
```

* Cria um estilo CSS básico e o adiciona como um item do livro.

10. **Definição da ordem de leitura (spine):**

```python
book.spine = ['nav', chapter]
```

* Define a sequência de leitura do EPUB. Aqui, o primeiro item será a navegação (`nav`), seguido pelo capítulo.

11. **Escrita do arquivo EPUB final:**

```python
epub.write_epub(output_epub_path, book, {})
```

* Salva o livro gerado no caminho especificado (`output_document.epub`).

12. **Envio do EPUB ao usuário:**

```python
context.bot.send_document(chat_id=update.effective_chat.id, document=open(output_epub_path, 'rb'))
```

* Envia o arquivo EPUB gerado de volta para o usuário no chat onde a mensagem original foi recebida.

13. **Função principal (`main`) — configuração do bot:**

```python
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
```

* Inicializa o `Updater` com o token e obtém o `dispatcher` para registrar os handlers.

---

```python
dp.add_handler(MessageHandler(Filters.document & ~Filters.command, convert_document_to_epub))
```

* Adiciona um handler que escuta **documentos enviados** que **não sejam comandos**, e ativa a função `convert_document_to_epub`.

---

```python
updater.start_polling()
updater.idle()
```

* Inicia o bot e o mantém em execução até que seja interrompido manualmente (ex: `Ctrl+C`).

14. **Bloco principal:**

```python
if __name__ == '__main__':
    main()
```

* Garante que a função `main()` só será executada se o script for rodado diretamente.

## INSTRUÇÃO:
Para converter documentos em vários formatos para EPUB, você pode usar a biblioteca ebooklib em Python. Veja o exemplo no [MAIN.PY](./CODIGO/MAIN.py)

Certifique-se de instalar as bibliotecas necessárias antes de executar o código:

```bash
pip install EbookLib
```