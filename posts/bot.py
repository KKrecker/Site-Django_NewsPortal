import telebot
from dotenv import load_dotenv
import os
load_dotenv()
token=os.getenv('TG_TOKEN')
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,f"Привет ✌️ {message.chat.id}")


if __name__ == '__main__':
    bot.infinity_polling()