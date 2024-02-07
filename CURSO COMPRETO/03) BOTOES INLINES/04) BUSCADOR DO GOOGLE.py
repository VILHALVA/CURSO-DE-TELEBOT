from TOKEN import *
import telebot
from googlesearch import search
from telebot import types 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "OLÁ! EU SOU O BUSCADOR DO GOOGLE. ENVIE O COMANDO '/buscar ASSUNTO'" )

resultados_da_pesquisa = {}

@bot.message_handler(commands=['buscar'])
def cmd_buscar(message):
    texto_buscar = " ".join(message.text.split()[1:])
    if not texto_buscar:
        texto = "VOCÊ DEVE FAZER UMA BUSCA\n"
        texto += "EXEMPLO\n"
        texto += f"<code>{message.text} frikendoth</code>\n"
        bot.send_message(message.chat.id, texto, parse_mode="html")
        return

    print(f"BUSCANDO NA GOOGLE: '{texto_buscar}'")
    try:
        resultados = list(search(texto_buscar, num_results=100))
        if not resultados:
            bot.send_message(message.chat.id, "Nenhum resultado encontrado.")
            return

        resultados_da_pesquisa[message.chat.id] = {
            "resultados": resultados,
            "indice": 0,
            "mensagem_anterior": None  
        }
        
        print("Resultados da pesquisa:")
        for i, resultado in enumerate(resultados):
            print(f"{i + 1}. {resultado}")

        enviar_resultado(message.chat.id, 0)

    except Exception as e:
        print(f"Erro na busca: {e}")
        bot.send_message(message.chat.id, "Erro na busca. Tente novamente mais tarde.")

def enviar_resultado(chat_id, indice):
    if chat_id in resultados_da_pesquisa:
        dados_pesquisa = resultados_da_pesquisa[chat_id]
        resultados = dados_pesquisa["resultados"]
        if 0 <= indice < len(resultados):
            resultado = resultados[indice]

            markup = types.InlineKeyboardMarkup()

            botoes_numerados = []

            if indice > 0:
                botoes_numerados.append(types.InlineKeyboardButton("Anterior", callback_data=f"anterior"))
            if indice < len(resultados) - 1:
                botoes_numerados.append(types.InlineKeyboardButton("Próximo", callback_data=f"proximo"))

            markup.row(*botoes_numerados)

            markup.add(types.InlineKeyboardButton("Abrir Link", url=resultado))

            mensagem_anterior = dados_pesquisa.get("mensagem_anterior")
            texto_mensagem = f"Resultado {indice + 1} de {len(resultados)}:\n{resultado}"

            if mensagem_anterior and mensagem_anterior.text != texto_mensagem:
                bot.edit_message_text(chat_id=chat_id, message_id=mensagem_anterior.message_id, text=texto_mensagem, reply_markup=markup)
            elif not mensagem_anterior:
                mensagem = bot.send_message(chat_id, texto_mensagem, reply_markup=markup)
                dados_pesquisa["mensagem_anterior"] = mensagem

            dados_pesquisa["indice"] = indice

@bot.callback_query_handler(func=lambda call: call.data in ('anterior', 'proximo'))
def callback_paginacao(call):
    chat_id = call.message.chat.id
    acao = call.data

    if chat_id in resultados_da_pesquisa:
        dados_pesquisa = resultados_da_pesquisa[chat_id]
        indice_atual = dados_pesquisa["indice"]

        if acao == 'anterior' and indice_atual > 0:
            enviar_resultado(chat_id, indice_atual - 1)
        elif acao == 'proximo' and indice_atual < len(dados_pesquisa["resultados"]) - 1:
            enviar_resultado(chat_id, indice_atual + 1)

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")