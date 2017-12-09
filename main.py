# -*- coding: utf-8 -*-
import sys

import telebot
import constants
import time

reload(sys)
sys.setdefaultencoding('utf-8')

bot = telebot.TeleBot(constants.token)  # makes token telebot object

upd = bot.get_updates()  # get all update info in JSON

listOfIdeas = []

try:
    last_upd = upd[-1]  # last chat update
    message_from_user = last_upd.message
except IndexError:
    last_upd = 0


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,
                                                    False)  # 1 - allocate buttons on the screen, 2 - Disappearing after click
    user_markup.row('Get Array', 'Clean Array') # add buttons to the row
    bot.send_message(message.from_user.id, 'Halo! You are using TelegramBot', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])  # means that this function will starts when available data comes
def handle_text(message):
    if message.from_user.first_name == 'Your username': # Constantly check if it's you
        try:
            print str("Message: " + message.text), str('    First name: ' + message.from_user.first_name), str(
                "      Username: " + message.from_user.username), str(time.strftime("     Time: %I:%M:%S\n"))
        except TypeError:
            pass

        if message.text == 'Get Array':
            try:
                bot.send_message(message.chat.id, ''.join(str(k) for k in listOfIdeas))
            except Exception:
                pass
        elif message.text == 'Clean Array':
            global listOfIdeas
            listOfIdeas = []
        else:
            # listOfIdeas.append(message.text)
            listOfIdeas.append(message.text + '\n')
    else:
        bot.send_message(message.chat.id, 'You shall not pass!!!')


bot.polling(none_stop=True, interval=0)
