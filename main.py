import telebot
import os
import datetime
import config
from telebot import types
import locale

token = config.API_BOT_TOKEN
bot = telebot.TeleBot(token)
current_azs = 0

locale.setlocale(locale.LC_TIME, 'ru')
dt_obj = datetime.datetime.now()
dt_string = dt_obj.strftime("%d-%b")

@bot.message_handler(commands=['start'])
def button_message(message):
    bot.send_message(message.chat.id, text=dt_string)
    # Проверяем наличие целевой папки с фото  создем при отсутствии
    if not os.path.isdir('C:/Users/spk-ws011/Desktop/foto/photos/'+dt_string):
        os.mkdir('C:/Users/spk-ws011/Desktop/foto/photos/'+dt_string)
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


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "АЗС 1":
        bot.send_message(message.chat.id, text="Загрузите фото АЗС 1:")
        current_azs = 1

    elif message.text == "АЗС 3":
        bot.send_message(message.chat.id, text="Загрузите фото АЗС 3:")
        current_azs = 3


@bot.message_handler(content_types=["photo"])
def photo(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = "C:/Users/spk-ws011/Desktop/foto/" + file_info.file_path
    with open(src, "wb") as new_file:
        new_file.write(downloaded_file)
    # bot.reply_to(message, "Фото получены, выберете следующую АЗС")


bot.polling(none_stop=True, interval=0)
