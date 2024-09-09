from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Function to start the bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I can help you download movies. Just send me the name of the movie.')

# Function to handle messages
def handle_message(update: Update, context: CallbackContext):
    movie_name = update.message.text
    # Here you would add the logic to find and send the movie link
    update.message.reply_text(f"Searching for {movie_name}...")

def main():
    # Add your bot's API token
    TOKEN = '7283978804:AAEYW4sAbQDEZdKiURBr2qopjZi_l_rhw4Y'
    
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
