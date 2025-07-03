from CONFIG import bot
from time import sleep

@bot.message_handler(commands=['ajuda'])
def mensagem_ajuda(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    resposta = (
        "Aqui estão os comandos disponíveis:\n\n"
        "*/start* - Inicia a interação com o bot\n"
        "*/ajuda* - Mostra esta mensagem de ajuda\n"
        "*/somar valor1 valor2* - Calcula a soma de dois valores\n"
        "*/subtrair valor1 valor2* - Calcula a subtração de dois valores\n"
        "*/multiplicar valor1 valor2* - Calcula a multiplicação de dois valores\n"
        "*/dividir valor1 valor2* - Calcula a divisão de dois valores\n"
    )

    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def mensagem_inicio(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(
        message.chat.id,
        "Olá! Eu sou um bot de cálculo. Como posso ajudar você? Envie /ajuda para saber mais!",
        parse_mode="Markdown"
    )

def obter_valores_argumentos(message):
    try:
        partes = message.text.strip().split()
        if len(partes) != 3:
            raise ValueError("Quantidade incorreta de argumentos.")
        return float(partes[1]), float(partes[2])
    except ValueError:
        return None, None

@bot.message_handler(commands=['somar'])
def mensagem_soma(message):
    v1, v2 = obter_valores_argumentos(message)
    if v1 is None or v2 is None:
        bot.reply_to(message, "Uso correto: /somar valor1 valor2")
        return

    resultado = v1 + v2
    bot.reply_to(message, f"O resultado da soma é: {resultado}")

@bot.message_handler(commands=['subtrair'])
def mensagem_subtracao(message):
    v1, v2 = obter_valores_argumentos(message)
    if v1 is None or v2 is None:
        bot.reply_to(message, "Uso correto: /subtrair valor1 valor2")
        return

    resultado = v1 - v2
    bot.reply_to(message, f"O resultado da subtração é: {resultado}")

@bot.message_handler(commands=['multiplicar'])
def mensagem_multiplicacao(message):
    v1, v2 = obter_valores_argumentos(message)
    if v1 is None or v2 is None:
        bot.reply_to(message, "Uso correto: /multiplicar valor1 valor2")
        return

    resultado = v1 * v2
    bot.reply_to(message, f"O resultado da multiplicação é: {resultado}")

@bot.message_handler(commands=['dividir'])
def mensagem_divisao(message):
    v1, v2 = obter_valores_argumentos(message)
    if v1 is None or v2 is None:
        bot.reply_to(message, "Uso correto: /dividir valor1 valor2")
        return

    if v2 == 0:
        bot.reply_to(message, "Não é possível dividir por zero.")
        return

    resultado = v1 / v2
    bot.reply_to(message, f"O resultado da divisão é: {resultado}")

@bot.message_handler(func=lambda message: True)
def mensagem_desconhecida(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.reply_to(message, "Desculpe, não entendi o que você disse.")

if __name__ == '__main__':
    bot.polling(timeout=20)
