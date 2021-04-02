import telebot
from telebot import types

TOKEN = '1320909136:AAHShEvqcKvHhhwjxoJM3RN0bomn1yXoGYY'
bot = telebot.TeleBot(TOKEN)

vw = 'VolksWagen'
hyundai = 'Hyundai'
kia = 'Kia'

vwClicks, hyundaiClicks, kiaClicks = 0, 0, 0 


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Это Письменный Даниил и его лабораторная!')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in [vw, hyundai, kia]])
    msg = bot.send_message(m.chat.id, 'Какую модель выбираешь?', reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def handle(m):
    global hyundaiClicks
    global kiaClicks
    global vwClicks

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if m.text == vw:
        keyboard.add(*[types.KeyboardButton(name) for name in ['Polo', 'Golf']])
        m = bot.send_message(m.chat.id, 'Данную марку выбрали ' + str(vwClicks) + ' раз.', reply_markup=keyboard)
        m = bot.send_message(m.chat.id, 'Какую модель выбираешь?', reply_markup=keyboard)
        vwClicks += 1
    
    elif m.text == kia:
        keyboard.add(*[types.KeyboardButton(name) for name in ['Rio', 'Ceed']])
        m = bot.send_message(m.chat.id, 'Данную марку выбрали ' + str(kiaClicks) + ' раз.', reply_markup=keyboard)
        m = bot.send_message(m.chat.id, 'Какую модель выбираешь?', reply_markup=keyboard)
        kiaClicks += 1

    elif m.text == hyundai:
        keyboard.add(*[types.KeyboardButton(name) for name in ['Solaris']])
        m = bot.send_message(m.chat.id, 'Данную марку выбрали ' + str(hyundaiClicks) + ' раз.', reply_markup=keyboard)
        m = bot.send_message(m.chat.id, 'Какую модель выбираешь?', reply_markup=keyboard)
        hyundaiClicks += 1

    else:
        if m.text == 'Solaris':
            bot.send_message(m.chat.id, 'Ну и выбор...')
        else: 
            bot.send_message(m.chat.id, 'Прекрасный выбор!')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [vw, hyundai, kia]])
        msg = bot.send_message(m.chat.id, 'Какую модель выбираешь?', reply_markup=keyboard)

bot.polling(none_stop=True)

