from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
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
    diction = {'tong': temp_c['morn'],
               'kun': temp_c['eve'],
               'oqshom': temp_c['night'],
               'min': temp_c['min'],
               'max': temp_c['max'],
               'namlik': w_day.humidity,
               'shamol': w_day.wnd,
               }
    print(diction)
    return diction

get_today_weather_data(w_first_day)
# pprint.pprint(w_daily)
# print(w_hourly)
# print(w_daily)