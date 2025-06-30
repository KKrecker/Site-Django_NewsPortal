import telebot
token="7517946921:AAHFuJKDuDOQL3YIsOBZ2WufSrIbtxnt3C0"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,f"Привет ✌️ {message.chat.id}")


if __name__ == '__main__':
    bot.infinity_polling()