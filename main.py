import schedule
import telebot
from threading import Thread
from time import sleep
from utils import get_today_weather_data, w_first_day

from config import TOKEN

bot = telebot.TeleBot(TOKEN)
some_id = "@pogodas"


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
    dictionary = get_today_weather_data(w_first_day)
    print(dictionary)
    cur_day = dictionary['current_day']
    sunrise = dictionary['chiqish']
    sunset = dictionary['botish']
    morn = round(dictionary['tong'])
    aft = round(dictionary['kun'])
    night = round(dictionary['oqshom'])
    min = round(dictionary['min'])
    max = round(dictionary['max'])
    namlik = round(dictionary['namlik'])
    status_ico = dictionary['status_ico']
    detail_status_ico = dictionary['detail_status_ico']
    ru_text = f"Сегодня, {cur_day}\n" \
              f"{status_ico + '+' + str(max) + '°' if max > 0 else status_ico + '-' + str(max) + '°'} " \
              f"{'+' + str(min) + '°' if min > 0 else '-' + str(min) + '°'}\n" \
              f"{detail_status_ico} Утром {morn}°\n" \
              f"{detail_status_ico} Днем {aft}°\n" \
              f"{detail_status_ico} Вечером {night}°\n\n" \
              f"Влажность: {namlik}%\n" \
              f"Восход: {sunrise}\nЗакат: {sunset}" # noqa

    uz_text = f"Bugun, {cur_day}\n" \
              f"{status_ico + '+' + str(max) + '°' if max > 0 else status_ico + '-' + str(max) + '°'} " \
              f"{'+' + str(min) + '°' if min > 0 else '-' + str(min) + '°'}\n" \
              f"{detail_status_ico} Tong {morn}°\n" \
              f"{detail_status_ico} Kun {aft}°\n" \
              f"{detail_status_ico} Oqshom {night}°\n\n" \
              f"Namlik: {namlik}%\n" \
              f"Quyosh chiqishi: {sunrise}\nQuyosh botishi: {sunset}" # noqa

    return ru_text, uz_text


x, y = get_text()


def function_to_run():
    return bot.send_message(some_id, x, disable_notification=True), bot.send_message(some_id, y,
                                                                                     disable_notification=True)


if __name__ == "__main__":
    # Create the job in schedule.
    schedule.every().day.at("03:06").do(function_to_run)
    # schedule.every(10).seconds.do(function_to_run)

    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start()
    # bot.polling()
    # And then of course, start your server.
