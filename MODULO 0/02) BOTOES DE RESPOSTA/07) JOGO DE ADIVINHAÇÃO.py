from TOKEN import *
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

bot = telebot.TeleBot(TOKEN)

# Dicionário para armazenar o estado do jogo para cada usuário
game_states = {}

@bot.message_handler(commands=["start"])
def start_game(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for num in range(1, 11):
        markup.add(KeyboardButton(str(num)))
    
    bot.reply_to(message, "Bem-vindo ao jogo de adivinhação! Escolha um número de 1 a 10:", reply_markup=markup)
    game_states[message.chat.id] = {"state": "waiting_for_guess", "correct_number": random.randint(1, 10)}

@bot.message_handler(func=lambda message: game_states.get(message.chat.id)["state"] == "waiting_for_guess" and message.text.isdigit())
def guess_number(message):
    guessed_number = int(message.text)
    correct_number = game_states[message.chat.id]["correct_number"]
    
    if guessed_number == correct_number:
        bot.reply_to(message, f"Parabéns! Você adivinhou o número corretamente: {correct_number}")
        game_states[message.chat.id]["state"] = None
    else:
        if guessed_number < correct_number:
            bot.reply_to(message, "O número que você escolheu é maior do que o número correto.")
        else:
            bot.reply_to(message, "O número que você escolheu é menor do que o número correto.")

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling()
    print("FIM")
