from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = r"YOUR_TOKEN"

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Ethathu sollu da pundaaa 😊")

def main():
    app = Application.builder().token(TOKEN).build()

    # Command handler for /start
    app.add_handler(CommandHandler("start", start))

    # Start polling
    app.run_polling()

if __name__ == "__main__":
    main()
