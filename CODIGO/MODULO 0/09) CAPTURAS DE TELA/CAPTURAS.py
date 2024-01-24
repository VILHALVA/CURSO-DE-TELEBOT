from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import telebot
import os
import pyscreenshot

TOKEN = "TOKEN_AQUI" # Substitua pelo Token do seu bot
ADMIN = "ID_AQUI"  # Substitua pelo seu ID de administrador
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.send_message(m.chat.id, "OLÁ! SEJA BEM VINDO AO CHAT COM O BOT!")

@bot.message_handler(commands=["cid"])
def cmd_cid(m):
    bot.send_message(m.chat.id, str(m.chat.id))

@bot.message_handler(commands=['1'])
def cmd_print_1(m):
    if es_admin(m.chat.id):
        print("TELA CAPTURADA!")
        captura = pyscreenshot.grab()
        print("GUARDANDO PRINT!")
        captura.save("captura.jpg")
        print("ENVIANDO PRINT!")
        with open("captura.jpg", "rb") as photo:
            bot.send_photo(m.chat.id, photo, caption="captura do servidor")
        print("ELIMINDANDO CAPTURA!")
        os.remove("captura.jpg")

@bot.message_handler(commands=['2'])
def cmd_print_2(m):
    if es_admin(m.chat.id):
        print("TELA CAPTURADA NO NAVEGADOR!")
        driver.save_screenshot("captura_chrome.png")
        print("GUARDANDO PRINT!")
        print("ENVIANDO PRINT!")
        with open("captura_chrome.png", "rb") as photo:
            bot.send_photo(m.chat.id, photo, caption="captura do chrome")
        print("ELIMINDANDO CAPTURA!")
        os.remove("captura_chrome.png")
        print("SELECIONANDO ELEMENTO")
        e = driver.find_element(By.CSS_SELECTOR, "header.entry-header")
        print("CAPTURANDO ELEMENTO!")
        e.screenshot("captura_elemento.png")
        print("GUARDANDO PRINT!")
        print("ENVIANDO PRINT!")
        with open("captura_elemento.png", "rb") as photo:
            bot.send_photo(m.chat.id, photo, caption="captura do elemento")
        print("ELIMINDANDO CAPTURA!")
        os.remove("captura_elemento.png")
        
@bot.message_handler(commands=['html'])
def cmd_html(m):
    if es_admin(m.chat.id):
        with open("pagina.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("ENVIANDO PÁGINA HTML!")
        bot.send_document(m.chat.id, open("pagina.html", "rb"))
        print("ELIMINANDO ARQUIVO HTML!")
        os.remove("pagina.html")

@bot.message_handler(commands=["point"])
def cmd_point(m):
    breakpoint()
    
def es_admin(cid, info=True):
    if cid == ADMIN:
        return True
    else:
        if info:
            print(f"{cid} NÃO ESTÁ AUTORIZADO!")
            bot.send_message(cid, f"<b>{cid} NÃO ESTÁ AUTORIZADO!</b>", parse_mode="html")
        return False

def web_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    ruta = ChromeDriverManager().install()
    lista = [
        "enable-automation",
        "enable-logging"
    ]
    options.add_experimental_option("excludeSwitches", lista)
    s = Service(ruta)
    driver = webdriver.Chrome(service=s, options=options)
    return driver

if __name__ == '__main__':
    print("INICIANDO O WEBDRIVER!")
    driver = web_driver()
    print("CARREGANDO O FRIKIDELTO.COM")
    driver.get("https://frikidelto.com")
    bot.infinity_polling(timeout=60)
