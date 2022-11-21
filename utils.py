import logging

from pyowm import OWM
from pyowm.weatherapi25.weather import Weather

import config
from datetime import datetime

# ---------- FREE API KEY examples ---------------------

owm = OWM(config.API_KEY)
mgr = owm.weather_manager()

# Search for current weather in Tashkent and get details
observation = mgr.one_call(lat=41.311081, lon=69.240562)
w_hourly = observation.forecast_hourly
w_first_day = observation.forecast_daily[0]


def get_today_weather_data(w_day: Weather, w_hourly_data: list):
    temp_c = w_day.temperature('celsius')
    status = {"Rain": "🌧",
              "light rain": "🌦",
              "None": "🌫️",
              "Thunderstorm": "⛈",
              "Drizzle": "🌧",
              "Snow": "🌨",
              "Mist": "🌫",
              "Clear": "☀️",
              "Clouds": "☁️",
              }

    # short = {'11d': "⛈",
    #          '10d': "🌦",
    #          '09d': "🌧",
    #          '13d': "🌨",
    #          '50d': "🌫️",
    #          '01d': "☀️",
    #          '01n': "☀️",
    #          '02d': "⛅️",
    #          '02n': "⛅️",
    #          '03d': "☁️",
    #          '03n': "☁️",
    #          '04d': "☁️",
    #          '04n': "☁️",
    #          }
    diction = {'min': temp_c['min'],
               'max': temp_c['max'],
               'namlik': w_day.humidity,
               'chiqish': datetime.fromtimestamp(w_day.sunrise_time()).strftime("%H:%M"),
               'botish': datetime.fromtimestamp(w_day.sunset_time()).strftime("%H:%M"),
               'current_day': datetime.fromtimestamp(w_day.reference_time()).strftime("%d %b"),
               'status_ico': status.get(w_day.status, "None"),
               'detailed_text': ((status.get(i.status, "None"), i.temperature('celsius')['temp'],
                                  i.temperature('celsius')['feels_like']) for i in w_hourly_data[:24]
                                 if datetime.fromtimestamp(i.ref_time).hour in (7, 13, 21))
               }
    logging.info(f"Bugungi statistika: {diction}")
    return diction


# print(get_today_weather_data(w_first_day, w_hourly))
