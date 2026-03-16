import time
import telebot
TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

while True:
    # Service tetap hidup di background
    time.sleep(60)
