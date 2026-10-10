import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا والله! بوت سكني شغال ✅\nارسل رقم هويتك للبحث")

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"استلمت: {update.message.text}\n(جاري ربطه مع موقع سكني قريبا)")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))
    await app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    import asyncio
    asyncio.run(main())
