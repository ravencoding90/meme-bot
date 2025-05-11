import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut, envoie-moi un Contract Address (CA) et je vais l’analyser.")

if name == 'main':
    app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
