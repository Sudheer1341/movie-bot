from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Function to start the bot
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! I can help you download movies. Just send me the name of the movie.')

# Function to handle messages
async def handle_message(update: Update, context: CallbackContext):
    movie_name = update.message.text
    # Here you would add the logic to find and send the movie link
    await update.message.reply_text(f"Searching for {movie_name}...")

async def main():
    # Add your bot's API token
    TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await application.start_polling()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
