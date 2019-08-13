from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import subprocess

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Wystartowałem!')


def help(bot, update):
    update.message.reply_text('To nie może byc takie proste...')

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def mstat(bot, update):
    ret="Odpowiedź PI:"
    ret=ret+str(subprocess.check_output("sudo systemctl status motion", shell=True))
    update.message.reply_text(ret)
def mstart(bot, update):
    ret="Odpowiedź PI:"
    ret = ret+str(subprocess.check_output("sudo systemctl start motion", shell=True))
    update.message.reply_text(ret)
def mstop(bot, update):
    ret="Odpowiedź PI:"
    ret = ret+str(subprocess.check_output("sudo systemctl stop motion", shell=True))
    update.message.reply_text(ret)
def main():
    with open('bot.key') as f:
        key = f.readline()
    updater = Updater(key)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("mstat", mstat))
    dp.add_handler(CommandHandler("mstart", mstart))
    dp.add_handler(CommandHandler("mstop", mstop))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
	main()
