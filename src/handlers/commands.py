import os
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

from ..services.weather import get_weather_text
from ..services.quotes import random_quote
from ..services.memes import random_meme
from ..services.calendar_stub import calendar_help_text


async def weather_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /weather <city>")
        return
    city = " ".join(context.args)
    text = await get_weather_text(city)
    await update.message.reply_text(text)

async def quote_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(random_quote())

async def meme_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(random_meme())

async def events_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(calendar_help_text())

def register_command_handlers(app: Application) -> None:
    app.add_handler(CommandHandler("weather", weather_cmd))
    app.add_handler(CommandHandler("quote", quote_cmd))
    app.add_handler(CommandHandler("meme", meme_cmd))
    app.add_handler(CommandHandler("events", events_cmd))