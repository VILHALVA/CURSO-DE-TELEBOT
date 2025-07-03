# COMANDOS VIA BARRA (/)
## DESCRIÇÃO:
Este é um exemplo de código em Python que demonstra como criar um bot do Telegram que fornece informações sobre qualquer assunto. O bot responde aos comandos `/[NOME DO COMANDO]`.

## EXPLICAÇÃO:
1. **Handler para os comandos `/start` e `/menu` com função personalizada:**

```python
@bot.message_handler(func=verificar, commands=["start", "menu"])
def responder(mensagem):
    texto = '''😁Olá. Eu sou bot de guia de linguagens de programação.'''
    sleep(1)
    texto = '''
🖥PRINCIPAIS LINGUAGENS DE PROGRAMAÇÃO:

/python > Linguagem Python
/js > Linguagem Java Script
/php > Linguagem PHP
/java > Linguagem JAVA
/ruby > Linguagem Ruby
/cplusplus > Linguagem C++
/csharp > Linguagem C#
/outros > Outras Linguagens de Programação

🌝BASTA APENAS CLICAR EM CIMA DE UMA OPÇÃO!
'''
    bot.reply_to(mensagem, texto)
```

* Esse trecho cria um **handler** que responde quando o usuário envia `/start` ou `/menu`.
* A função `verificar(mensagem)` é usada como filtro adicional e deve retornar `True` para que o handler seja ativado (no código fornecido, ela sempre retorna `True`).
* O bot responde com uma mensagem introdutória e, logo depois, exibe uma lista de comandos com as linguagens disponíveis.

2. **Handler para cada linguagem de programação individual:**

Exemplo com Python:

```python
@bot.message_handler(commands=["python"])
def python(mensagem):
    bot.send_message(mensagem.chat.id, "Python é uma linguagem de programação de alto nível...🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Python")
```

* Esse padrão se repete para comandos como `/js`, `/php`, `/java`, `/ruby`, `/cplusplus`, `/csharp`, `/outros`.
* Quando o usuário envia uma mensagem com um desses comandos, o bot responde com uma descrição detalhada da linguagem correspondente, seguida de um link para saber mais.

