import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import asyncio

TOKEN = "7695005663:AAGXkSE3PPp352oTKGiOyO4C5i24W9nQSVY"  # Встав свій токен сюди

TRIGGER_WORDS = ["роздрукувати", "видрукувати", "друк", "принтер"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        if any(word in text for word in TRIGGER_WORDS):
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="З друком допоможе @Viperiukr"
            )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Бот запущено. Очікую повідомлення в групі...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
