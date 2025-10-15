from telegram import Update

async def reply(update: Update, text: str) -> None:
    if update.message:
        await update.message.reply_text(text)