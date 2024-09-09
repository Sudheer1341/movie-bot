from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Function to handle the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Welcome! How can I assist you today?')

async def main():
    # Replace with your actual Telegram bot API token
    TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'

    # Create an Application instance with your bot token
    application = Application.builder().token(TOKEN).build()

    # Add a handler for the /start command
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    await application.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
