import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import pyaspeller
import os
from dotenv import load_dotenv
from transliterate import translit

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

speller = pyaspeller.YandexSpeller(lang='ru')

def fix_typos(text):
    """
    Fix common typos in Russian text using Yandex Speller.
    The function retrieves suggestions for misspelled words and replaces them
    in reverse order (so that earlier text positions are not affected by later changes).
    """
    corrections = speller.spell(text)
    if corrections:
        # Sort corrections in descending order of error position
        for error in sorted(corrections, key=lambda e: e['pos'], reverse=True):
            start = error['pos']
            length = len(error['word'])
            if error['s']:
                suggestion = error['s'][0]
                text = text[:start] + suggestion + text[start + length :]
    return text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text(
        "Привет!\nОтправь мне сообщение, в котором русские слова написаны латинскими буквами, "
        "и я переведу его в кириллицу, а также постараюсь исправить опечатки."
    )

async def transform_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Take the user's message, transliterate it from Latin to Cyrillic,
    fix typos using YandexSpeller, and then reply with the result.
    """
    input_text = update.message.text

    try:
        # Transliterate from Latin to Cyrillic
        transliterated_text = translit(input_text, 'ru')
    except Exception as e:
        logger.error("Transliteration error: %s", e)
        transliterated_text = input_text

    # Apply the typo fixer.
    fixed_text = fix_typos(transliterated_text)
    await update.message.reply_text(fixed_text)

def main():
    """Start the bot."""
    # Load the bot token from an environment variable.
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("No token provided. Set the TELEGRAM_BOT_TOKEN environment variable.")
        return

    application = Application.builder().token(token).build()

    # Register the /start command handler.
    application.add_handler(CommandHandler("start", start))
    # Register a message handler for processing text messages.
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, transform_text))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
