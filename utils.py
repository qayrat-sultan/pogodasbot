import logging

from pyowm import OWM
from pyowm.weatherapi25.weather import Weather

import config
from datetime import datetime

# ---------- FREE API KEY examples ---------------------

owm = OWM(config.API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.one_call(lat=41.311081, lon=69.240562)
w_hourly = observation.forecast_hourly
w_first_day = observation.forecast_daily[0]
w_humidity = observation.forecast_daily[0].humidity


def get_today_weather_data(w_day: Weather):
    temp_c = w_day.temperature('celsius')
    status = {"Rain": "🌧",
              "light rain": "🌦",
              "None": "☀️"}

    short = {'11d': "⛈",
             '10d': "🌦",
             '09d': "🌧",
             '13d': "🌨",
             '50d': "🌫️",
             '01d': "☀️",
             '01n': "☀️",
             '02d': "⛅️",
             '02n': "⛅️",
             '03d': "☁️",
             '03n': "☁️",
             '04d': "☁️",
             '04n': "☁️",
             }
    diction = {'tong': temp_c['morn'],
               'kun': temp_c['eve'],
               'oqshom': temp_c['night'],
               'min': temp_c['min'],
               'max': temp_c['max'],
               'namlik': w_day.humidity,
               'chiqish': datetime.fromtimestamp(w_day.sunrise_time()).strftime("%H:%M"),
               'botish': datetime.fromtimestamp(w_day.sunset_time()).strftime("%H:%M"),
               'current_day': datetime.fromtimestamp(w_day.reference_time()).strftime("%d %b"),
               # 'ico': short[w_day.weather_icon_name],
               'status_ico': status.get(w_day.status, "None"),
               'detail_status_ico': status.get(w_day.detailed_status, "None")
               }
    logging.info(f"Bugungu statistika: {diction}")
    return diction