import telegram 
import serial
import time
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Eh we, qué onda?')
    # print('')
    
bot = telegram.Bot(token='765791498:AAG1FkapzuXtXFZrVU27WdAzUey6xtnkH00')
update = Updater(token='765791498:AAG1FkapzuXtXFZrVU27WdAzUey6xtnkH00')
dispatcher = update.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

update.start_polling()
