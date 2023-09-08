# BOTÕES INLINES
## CRIANDO BOTÕES:
Você criou um objeto `InlineKeyboardMarkup` chamado `marca` com um `row_width` de 2. Isso significa que, quando você adicionar botões a este teclado inline, eles serão organizados em linhas contendo no máximo 2 botões cada.

Você pode usar esse `InlineKeyboardMarkup` para criar botões inline em mensagens e fornecer opções de resposta ao usuário em uma conversa no Telegram. A propriedade `row_width` permite controlar quantos botões são exibidos em cada linha do teclado.

Aqui está um exemplo de como adicionar botões ao teclado `marca` com `InlineKeyboardButton`:

```python
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

marca = InlineKeyboardMarkup(row_width=2)

# Adicionar botões ao teclado
botao1 = InlineKeyboardButton("Opção 1", callback_data="opcao1")
botao2 = InlineKeyboardButton("Opção 2", callback_data="opcao2")
botao3 = InlineKeyboardButton("Opção 3", callback_data="opcao3")

# Adicionar os botões ao teclado, dois por linha
marca.add(botao1, botao2)
marca.add(botao3)
```

Neste exemplo, três botões são adicionados ao teclado `marca`, com dois botões por linha, conforme especificado pelo `row_width`. Esses botões podem ser usados em uma mensagem e, quando o usuário interage com eles, você pode processar as respostas usando os valores de `callback_data`.

O teclado inline é útil para criar interações mais avançadas com os usuários no Telegram, como seleção de opções em um menu ou votação em uma enquete.

## CALLBACK DATA:
```python
fechar = InlineKeyboardButton("FECHAR", callback_data="fechar")
marca.add(fechar)
#...
```
Agora, você tem um teclado inline com um botão "FECHAR" que pode ser usado em mensagens no Telegram. Quando o usuário interagir com esse botão, você pode processar a ação associada ao `callback_data` "fechar".

Você pode incorporar esse teclado inline em uma mensagem enviada pelo seu bot para fornecer aos usuários a opção de fechar alguma ação ou janela de chat, por exemplo. Quando o botão "FECHAR" for pressionado, o Telegram enviará a ação associada ("fechar") como um callback, que você pode então processar em seu código para realizar a ação desejada.

## FUNÇÃO LAMBDA:
```python
#...
@bot.callback_query_handler(func=lambda x: True)
def respostas(call):
    cid = call.from_user.id
    mid = call.message.id
    if call.data == "FECHAR":
        bot.delete_message(cid, mid)    
```
Você criou uma função `respostas` que lida com callbacks de botões inline. Neste caso, quando o botão "FECHAR" é pressionado e a ação associada é "fechar" (como especificado no `callback_data`), a função `respostas` é acionada.

Dentro da função, você obtém o `id` do usuário que fez a chamada (`cid`) e o `id` da mensagem original (`mid`) usando `call.from_user.id` e `call.message.id`, respectivamente.

Em seguida, você verifica se o `callback_data` é igual a "FECHAR". Se for, você usa `bot.delete_message()` para excluir a mensagem original. Isso permite que você feche ou remova alguma janela de chat ou ação específica quando o usuário pressionar o botão "FECHAR".

Essa função é útil para controlar as interações do usuário e realizar ações específicas com base nos botões inline pressionados. 

## REPRICANDO O BUSCAR DO GOOGLE:
Este é um bot Telegram em Python que permite realizar buscas no Google diretamente a partir do Telegram. O bot utiliza a biblioteca `telebot` para interagir com a API do Telegram e a biblioteca `googlesearch-python` para realizar as buscas.

Antes de usar o bot, certifique-se de que você tenha as seguintes dependências instaladas:
- Python 3.x
- Biblioteca `telebot`
- Biblioteca `googlesearch-python`

Agora, você pode interagir com o bot no Telegram. Envie o comando `/buscar` seguido da sua consulta, por exemplo:
   ```
   /buscar Como criar um bot Telegram em Python
   ```
   O bot responderá com os 100 resultados da pesquisa no Google.
   Com botões de "Anterior" "Proximo" (Ao clicar o bot edita a mesma mensagem) e "Abrir link" (Abri a url correspondente)

