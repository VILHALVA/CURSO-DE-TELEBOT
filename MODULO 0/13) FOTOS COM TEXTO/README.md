# FOTOS COM TEXTO
## DESCRIÇÃO:
O código se destina a criar um bot do Telegram que, quando o comando `/start` é acionado, envia uma mensagem de boas-vindas ao usuário. O comando `/foto` envia uma foto com uma descrição, e se a descrição for muito longa, a imagem é enviada como um link.

## REQUERIMENTOS:
1. **telebot:** Esta biblioteca é usada para criar um bot do Telegram e interagir com a API do Telegram.

2. **imagekitio:** Utilizada para trabalhar com imagens usando o serviço [ImageKit](https://imagekit.io/), que oferece recursos de gerenciamento de imagens.

3. **base64:** Importação da função `b64encode` da biblioteca base64 para codificar imagens em base64.

Além disso, você precisa ter um token válido para o seu bot do Telegram (`TOKEN`), chaves de acesso ao ImageKit (`IK_PUBLIC` e `IK_PRIVATE`), e uma URL de um endpoint do ImageKit (`IK_URL`) configurados no seu código.

## INSTALAÇÕES:
```bash
pip install imagekitio
```