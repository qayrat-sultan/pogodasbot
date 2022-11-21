import os
import logging
import datetime

from dotenv import load_dotenv

load_dotenv()

formatter = '[%(asctime)s] %(levelname)8s --- %(message)s (%(filename)s:%(lineno)s)'
logging.basicConfig(
    filename=f'bot-from-{datetime.datetime.now().date()}.log',
    filemode='w',
    format=formatter,
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.WARNING
)
API_KEY = os.environ.get("owm_key")

TOKEN = os.environ.get("token_pogodas")




