import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
BOT_TOKEN=os.environ.get("BOT_TOKEN")
app=Flask(__name__)
@app.route('/')
def home():return "sakani-bot is running!"
def run_web():app.run(host='0.0.0.0',port=int(os.environ.get("PORT",10000)))
threading.Thread(target=run_web,daemon=True).start()
async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):await update.message.reply_text("هلا والله! بوت سكني شغال ✅")
def main():
 a=ApplicationBuilder().token(BOT_TOKEN).build()
 a.add_handler(CommandHandler("start",start))
 a.run_polling()
if __name__=="__main__":main()
