# SECRETARIO VIA CONSOLE
Este é um exemplo simples de como criar um bot do Telegram em Python usando a biblioteca `requests` para interagir com a API do Telegram. O bot recebe mensagens de texto dos usuários e responde com informações relacionadas aos tópicos especificados.

## Requisitos
Certifique-se de ter instalado o Python em sua máquina. Além disso, você precisará da biblioteca `requests` para fazer solicitações HTTP à API do Telegram. Você pode instalar a biblioteca usando o seguinte comando:

```bash
pip install requests
```

## Configuração
1. Crie um bot no Telegram e obtenha o token do bot do BotFather.

2. Substitua `'YOUR_BOT_TOKEN'` na linha `TOKEN  = "YOUR_BOT_TOKEN"` pelo token real do seu bot.

## Executando o Bot
1. Execute o script Python. O bot começará a verificar novas mensagens e responderá de acordo.

## Funcionalidades
- O bot responde a mensagens de texto com base em algumas palavras-chave, como tecnologia, ciência, filosofia e teologia.

- O bot fornece informações sobre os tópicos mencionados, juntamente com algumas mensagens predefinidas.

- O bot envia respostas de volta para o usuário que enviou a mensagem original.

- Você recebe a mensagem que o usuário enviou no PV do bot dentro do console da sua IDE (Ou servidor). Daí você pode responde-lo diretamente pela IDE.

## Código de Exemplo
```python
import requests
import json
import os

class TelegramBot:
    def __init__(self):
        TOKEN  = "YOUR_BOT_TOKEN"
        self.iURL = f"https://api.telegram.org/bot{TOKEN}/"
    def Iniciar(self):
        iUPDATE_ID = None
        while True:
            ATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
            IDADOS = ATUALIZACAO["result"]
            if IDADOS:
                for dado in IDADOS:
                    iUPDATE_ID = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.gerar_respostas(mensagem, primeira_mensagem)
                    self.responder(resposta, chat_id)
                    
    # Omissão do código relacionado a ler_novas_mensagens e gerar_respostas
    
    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("=" *100,"\n🤖RESPONDIR:\n>>>" + str(resposta), "\n", "=" *100,)

bot = TelegramBot()
bot.Iniciar()
```

## Personalização
Este é um exemplo básico de um bot do Telegram que responde a mensagens de texto. Você pode personalizar e expandir o bot adicionando mais respostas, tópicos e funcionalidades, conforme necessário.

## Documentação
- [Telegram Bot API](https://core.telegram.org/bots/api): Documentação oficial da API do Telegram.

Lembre-se de que este é um exemplo de um bot simples, e você pode adicionar mais recursos e interatividade para criar um bot mais complexo e útil.