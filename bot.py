#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    kb = [[InlineKeyboardButton('Кафедра КМАД', callback_data = 'kafedra')],
          [InlineKeyboardButton('Можливості для студентів', callback_data = 'mozhlivosti')],
          [InlineKeyboardButton('Умови вступу', callback_data = 'umovy')]]
    reply = InlineKeyboardMarkup(kb)
    update.message.reply_text('Hi! You can choose', reply_markup = reply )
    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def bro(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("I'm bro, you are bro, we are brothers ")



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def kafedra(update, context):
    """Send a message when the command /start is issued."""
    kb = [[InlineKeyboardButton('Викладачі', callback_data = '')],
    [InlineKeyboardButton('Відмінності кафедри', callback_data = '')],
    [InlineKeyboardButton('Історія кафедри', callback_data = '')],
    [InlineKeyboardButton('Аудиторії кафедри', callback_data = '')],
    [InlineKeyboardButton('Наші випускники', callback_data = '')]]
    reply = InlineKeyboardMarkup(kb)
    update.callback_query.message.reply_text('З чого почнемо?', reply_markup = reply )
def mozhlivosti(update, context):
    pass
def umovy(update, context):
    kb = [[InlineKeyboardButton('Конкурсні предмети ЗНО',callback_data = '')],
          [InlineKeyboardButton('Розрахунок конкурсного балу',callback_data = '')],
          [InlineKeyboardButton('Етапи вступної компанії',callback_data = '')],
          [InlineKeyboardButton('Корисні посилання',callback_data = '')],
          [InlineKeyboardButton('Кількість бюджетних та контрактних мість для вступників',callback_data = '')],]
    reply = InlineKeyboardMarkup(kb)
    update.callback_query.message.reply_text('Hi! you can choose', reply_markup = reply )
def main():

    updater = Updater("1600092846:AAHLA--iPlmFI8LMfp-U7PEL2NtmrGqUJJQ", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("bro", bro))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = 'kafedra'))
    dp.add_handler(CallbackQueryHandler(mozhlivosti, pattern = 'mozhlivosti'))
    dp.add_handler(CallbackQueryHandler(umovy, pattern = 'umovy'))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
