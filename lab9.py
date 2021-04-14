import telebot
from telebot import types

TOKEN = '1320909136:AAHShEvqcKvHhhwjxoJM3RN0bomn1yXoGYY'
bot = telebot.TeleBot(TOKEN)

hyundai = 'Hyundai'
like_values = ['Нравится', 'Не нравится']
questionMessage = 'Как оцениваете производителя?'
hyundai_likes = 0
hyundai_dislikes = 0


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Это Письменный Даниил и его лабораторная!')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in like_values])
    m = bot.send_message(m.chat.id, questionMessage + ' ' + hyundai, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda m: m.data)
def like(m):
    global hyundai_likes
    global hyundai_dislikes

    if m.data == like_values[0]:
        hyundai_likes += 1
        bot.send_message(m.message.chat.id, 'Данная марка понравилась ещё ' + str(hyundai_likes) + ' раз')
    else:
        hyundai_dislikes += 1
        bot.send_message(m.message.chat.id, 'Данная марка не понравилась ещё ' + str(hyundai_dislikes) + ' раз')

    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in like_values])
    m = bot.send_message(m.message.chat.id, questionMessage + ' ' + hyundai, reply_markup=keyboard)


bot.polling(none_stop=True)
