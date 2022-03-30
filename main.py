import schedule
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from threading import Thread
from time import sleep
from utils import get_today_weather_data, w_first_day, w_hourly

from config import TOKEN

bot = telebot.TeleBot(TOKEN)
some_id = "@pogodas"
# some_id = 390736292


@bot.message_handler()
def some_text(message: telebot.types.Message):
    print(message)
    x = function_to_run()
    print(x)


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def get_text():
    dictionary = get_today_weather_data(w_first_day, w_hourly)
    cur_day = dictionary['current_day']
    sunrise = dictionary['chiqish']
    sunset = dictionary['botish']
    min = round(dictionary['min'])
    max = round(dictionary['max'])
    namlik = round(dictionary['namlik'])
    status_ico = dictionary['status_ico']
    morning, afternoon, nightly = dictionary['detailed_text']
    ru_text = f"Сегодня, {cur_day}\n" \
              f"{status_ico} {'+' if max>0 else ''} {str(max)}° {'+' if min>0 else ''} {str(min)}°\n" \
              f"{morning[0]} Утром {'+' if morning[1]>0 else ''} {round(morning[1])}° " \
              f"(ощущается как {'+' if morning[2]>0 else ''} {round(morning[2])})\n" \
              f"{afternoon[0]} Днем {'+' if afternoon[1] > 0 else ''} {round(afternoon[1])}° " \
              f"(ощущается как {'+' if afternoon[2] > 0 else ''} {round(afternoon[2])})\n" \
              f"{nightly[0]} Вечером {'+' if nightly[1] > 0 else ''} {round(nightly[1])}° " \
              f"(ощущается как {'+' if nightly[2] > 0 else ''} {round(nightly[2])})\n" \
              f"Влажность: {namlik}%\n" \
              f"Восход: {sunrise}\nЗакат: {sunset}\n@pogodas" # noqa

    uz_text = f"Bugun, {cur_day}\n" \
              f"{status_ico} {'+' if max>0 else ''} {str(max)}° {'+' if min>0 else ''} {str(min)}°\n" \
              f"{morning[0]} Tong {'+' if morning[1]>0 else ''} {round(morning[1])}° " \
              f"({'+' if morning[2]>0 else ''} {round(morning[2])} kabi seziladi)\n" \
              f"{afternoon[0]} Kun {'+' if afternoon[1] > 0 else ''} {round(afternoon[1])}° " \
              f"({'+' if afternoon[2] > 0 else ''} {round(afternoon[2])} kabi seziladi)\n" \
              f"{nightly[0]} Oqshom {'+' if nightly[1] > 0 else ''} {round(nightly[1])}° " \
              f"({'+' if nightly[2] > 0 else ''} {round(nightly[2])} kabi seziladi)\n" \
              f"Namlik: {namlik}%\n" \
              f"Quyosh chiqishi: {sunrise}\nQuyosh botishi: {sunset}\n@pogodas" # noqa

    return ru_text, uz_text


x, y = get_text()


def function_to_run():
    # keyboard_ru = InlineKeyboardMarkup(row_width=1)
    # button_ru = InlineKeyboardButton("Другой город", url="https://t.me/pogodasuzbot?start=ru")
    # keyboard_ru.add(button_ru)
    # keyboard_uz = InlineKeyboardMarkup(row_width=1)
    # button_uz = InlineKeyboardButton("Boshqa shahar", url="https://t.me/pogodasuzbot?start=uz")
    # keyboard_uz.add(button_uz)
    return bot.send_message(some_id, x,
                            disable_notification=True), \
           bot.send_message(some_id, y,
                            disable_notification=True)


if __name__ == "__main__":
    # Create the job in schedule.
    schedule.every().day.at("03:06").do(function_to_run)
    # schedule.every(10).seconds.do(function_to_run)
    # function_to_run()
    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start()
    # bot.polling()
    # And then of course, start your server.
