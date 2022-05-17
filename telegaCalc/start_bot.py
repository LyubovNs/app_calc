from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
import logging
import venv

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

updater = None

def start_bot():
    global updater
    updater = Updater(
        '5352935775:AAENA4YzYLSlHp6jqdfI3mR9wOK89o7aGaw', use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(MessageHandler(Filters.text, repeater))  #повторитель

    dispatcher.add_handler(CommandHandler('echo', echo))

    updater.start_polling()

    venv.main()


def start(update, context):
    s = "Расчет зарплаты и аванса"
    update.message.reply_text(s)

def repeater(update, context):
    if context.user_data[echo]:
        update.message.reply_text(update.message.text)

def echo(update, context):
    command = context.args[0].lower()
    if ("on" == command):
        context.user_data[echo] = True
        update.message.reply_text("Repeater Started")
    elif ("off" == command):
        context.user_data[echo] = False
        update.message.reply_text("Repeater Stopped")




start_bot()




