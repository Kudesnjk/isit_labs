import requests
import telebot

TOKEN = '1320909136:AAHShEvqcKvHhhwjxoJM3RN0bomn1yXoGYY'
bot = telebot.TeleBot(TOKEN)

user_id = '84105524'
access_token = 'e4697c386550a5703318dc3973e5c32173de2a42ce27dbb6385811fd656a1fb31afd50a2b75aca6d3bd0c'


@bot.message_handler(content_types=["text"])
def handle_message(message):
    text = message.text
    r = requests.get(
        'https://api.vk.com/method/wall.post?owner_id={}&message={}&access_token={}&v=5.130'.format(user_id, text,
                                                                                                    access_token))
    print(r.json())
    if 'response' in r.json():
        bot.send_message(message.chat.id, 'Пост опубликован, его id = ' + str(r.json()['response']['post_id']))
    else:
        bot.send_message(message.chat.id, 'Ошибка при публикации поста')


bot.polling(none_stop=True)
