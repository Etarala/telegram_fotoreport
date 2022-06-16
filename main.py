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
    markup.add(*list(map(lambda x: types.KeyboardButton(x), get_azs_list())))
    bot.send_message(message.chat.id, 'Выберите АЗС и загрузите фото:', reply_markup=markup)


@bot.message_handler(regexp='^АЗС\s\d+$')
def func(message):
    global current_azs

    matches = re.search('^АЗС\s(\d+)+$', message.text)
    if message.text in get_azs_list():
        bot.send_message(message.chat.id, text="Загрузите фото " + matches[0] + ':')
        current_azs = matches[1]


@bot.message_handler(content_types=["photo"])
def photo(message):
    if not os.path.isdir(get_upload_folder_path()):
        os.makedirs(get_upload_folder_path(), exist_ok=True)

    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(convert_file_path(file_info.file_path), "wb") as new_file:
        new_file.write(downloaded_file)
    #bot.reply_to(message, "Фото получены, выберете следующую АЗС")


bot.polling(none_stop=True, interval=0)