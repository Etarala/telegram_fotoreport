import telebot
import os
import datetime
import config
from telebot import types
import locale
import re

token = config.API_BOT_TOKEN
bot = telebot.TeleBot(token)
current_azs = 0

locale.setlocale(locale.LC_TIME, 'ru')


def get_upload_folder_path() -> str:
    dt_obj = datetime.datetime.now()
    dt_string = dt_obj.strftime("%d-%b")
    return config.FOLDER_PATH + dt_string


def convert_file_path(file_path: str) -> str:
    global current_azs
    file_name = 'АЗС_' + str(current_azs) + '_' + file_path.split('/')[1]

    print(file_name)

    return os.path.join(get_upload_folder_path(), file_name)


def get_azs_list():
    return list(
        map(lambda x: "АЗС " + str(x), config.AZS_LIST)
    )

@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("АЗС 1")
    item2 = types.KeyboardButton("АЗС 3")
    item3 = types.KeyboardButton("АЗС 4")
    item4 = types.KeyboardButton("АЗС 5")
    item5 = types.KeyboardButton("АЗС 7")
    item6 = types.KeyboardButton("АЗС 9")
    item7 = types.KeyboardButton("АЗС 10")
    item8 = types.KeyboardButton("АЗС 11")
    item9 = types.KeyboardButton("АЗС 15")
    item10 = types.KeyboardButton("АЗС 17")
    item11 = types.KeyboardButton("АЗС 19")
    item12 = types.KeyboardButton("АЗС 21")
    item13 = types.KeyboardButton("АЗС 22")
    item14 = types.KeyboardButton("АЗС 23")
    item15 = types.KeyboardButton("АЗС 24")
    item16 = types.KeyboardButton("АЗС 25")
    item17 = types.KeyboardButton("АЗС 26")
    item18 = types.KeyboardButton("АЗС 27")
    item19 = types.KeyboardButton("АЗС 28")
    item20 = types.KeyboardButton("АЗС 30")
    item21 = types.KeyboardButton("АЗС 31")
    item22 = types.KeyboardButton("АЗС 32")
    item23 = types.KeyboardButton("АЗС 33")
    item24 = types.KeyboardButton("АЗС 35")
    item25 = types.KeyboardButton("АЗС 36")
    item26 = types.KeyboardButton("АЗС 37")
    item27 = types.KeyboardButton("АЗС 38")
    item28 = types.KeyboardButton("АЗС 39")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14,
               item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27,
               item28)
    bot.send_message(message.chat.id, 'Выберите АЗС и загрузите фото:', reply_markup=markup)


@bot.message_handler(regexp='^АЗС\s\d+$')
def func(message):
    global current_azs

    matches = re.search('^АЗС\s\d+$', message.text)
    if message.text in get_azs_list():
        bot.send_message(message.chat.id, text="Загрузите фото :" + matches[0] + ':')
        current_azs = matches[1]


@bot.message_handler(content_types=["photo"])
def photo(message):
    if not os.path.isdir(get_upload_folder_path()):
        os.makedirs(get_upload_folder_path(), exist_ok=True)

    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(convert_file_path(file_info.file_path), "wb") as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Фото получены, выберете следующую АЗС")


bot.polling(none_stop=True, interval=0)