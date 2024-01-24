import telebot
from telebot.types import InlineQueryResultArticle
from telebot.types import InputTextMessageContent
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("TOKEN AQUI")

def busar_google(texto):
    lista = []
    user_agent = 'mozilla/5.0 (Windows NT 10; win64 x64) Applewebkit/537.36(KHTML, like)'
    headers = {
        "User_Agent": user_agent,
        'referer': 'https://www.google.com/' 
    }
    
    texto_url = texto.replace(" ", "+")
    url = f'https://www.google.com/search?q={texto_url}&num=50'
    r = requests.get(url, headers=headers, timeout=10)
    if r.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        elementos = soup.find_all("div", {"class": "g"})
        for e in elementos:
            try:
                titulo = e.find_all("h3")[-1].text.split()
            except:
                continue
            
            descricao = e.find_all("span")[-1].text.split() 
            enlace = e.find("a").attrs.get("href")
            if titulo and enlace and not(titulo, descricao, enlace) in lista:
                lista.append((titulo, descricao, enlace))

    print(f"ENCONTRADOR {len(lista)} RESULTADOS!")
    return lista

@bot.inline_handler(lambda q: True)
def texto_inline(m):
    if not m.query:
        return
    print(f"BUSCANDO NO GOOGLE: {m.query}")
    res = busar_google(m.query) 
    
    if not res:
        print("NENHUM RESULTADO FOI ENCONTRADO!")
        return
    lista = []
    n = 0
    for titulo, descricao, url in res:
        n += 1
        obj = InlineQueryResultArticle(
            id=str(n),
            title=titulo,
            description=descricao,
            thumb_url='https://i.imgur.com/3P9qfX8.png',
            input_message_content=InputTextMessageContent(url),
        )
        lista.append(obj)
    if not lista:
        return
    try:
        bot.answer_inline_query(m.id, lista, cache_time=30)
    except Exception as e:
        print(e)
