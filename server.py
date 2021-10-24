from telegram import * 
from telegram.ext import *

TOKEN = '2057573270:AAH-33QCuMRQLehNRq6mbdS9R5xvUoAfba0'

bot = Bot(TOKEN)
updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher

def test(update:Update, context:CallbackContext):
	bot.send_message(
		chat_id = update.effective_chat.id,
		text="No orders yet",
	)


start_value = CommandHandler('get-orders', test)

dispatcher.add_handler(start_value)

updater.start_polling()