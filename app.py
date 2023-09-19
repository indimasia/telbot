import telebot

# Create a TeleBot instance
bot = telebot.TeleBot('6553586390:AAFq5rmgEnAbltPmqOMVa8c0OA_aEPfjQTc')

# Define a message handler for the `/start` command
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, 'Hello!')

@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.reply_to(message, 'What can I do for you?')

# Start the bot
bot.polling()
