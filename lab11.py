import datetime
import requests
import telebot
import xml.dom.minidom
import re
from telebot import types

TOKEN = '1320909136:AAHShEvqcKvHhhwjxoJM3RN0bomn1yXoGYY'
bot = telebot.TeleBot(TOKEN)

currencies = ['Йена', 'Австралийский доллар']
data_re = r'\d\d/\d\d/\d\d\d\d'

user_date_dict = {}


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Это Письменный Даниил и его лабораторная!')
    bot.send_message(m.chat.id, 'Введите интересующую дату, формат dd/mm/year')


@bot.message_handler(content_types=["text"])
def handle(m):
    global user_date_dict

    if m.text not in currencies:
        if not re.match(data_re, m.text):
            bot.send_message(m.chat.id, 'Некорректный формат даты')
            bot.send_message(m.chat.id, 'Введите интересующую дату, формат dd/mm/year')
            return
        user_date_dict[m.chat.id] = m.text
        bot.send_message(m.chat.id, 'Выберите валюту')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in currencies])
        return

    date = user_date_dict[m.chat.id]
    request = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + date
    r = requests.get(request)
    dom = xml.dom.minidom.parseString(r.text)
    dom.normalize()

    try:
        value = ''
        if m.text == currencies[0]:
            value = dom.getElementsByTagName('Valute')[33].childNodes[4].childNodes[0].nodeValue
            bot.send_message(m.chat.id,
                             'Курс {} по отношению к рублю на {} равен {}'.format(currencies[0], date, value))
        else:
            value = dom.getElementsByTagName('Valute')[0].childNodes[4].childNodes[0].nodeValue
            bot.send_message(m.chat.id,
                             'Курс {} по отношению к рублю на {} равен {}'.format(currencies[1], date, value))
    except IndexError:
        bot.send_message(m.chat.id, 'Некорректная дата')

    bot.send_message(m.chat.id, 'Введите интересующую дату, формат dd/mm/year')


bot.polling(none_stop=True)
