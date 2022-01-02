import requests
from bs4 import BeautifulSoup as bs
import schedule
import telebot
from threading import Thread
from time import sleep

from config import TOKEN

bot = telebot.TeleBot(TOKEN)
#some_id = 390736292 # This is our chat id.
some_id = "@pogodas"

links = ["https://pogoda.uz/tashkent", "https://obhavo.uz/tashkent"]



def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def get_text(links):
    ico_link_uz = "https://obhavo.uz/images/icons/"
    ico_link_ru = "https://pogoda.uz/images/icons/"
    icons = {"rain.png":"🌧", 
            "snow.png":"❄️", 
            "cloudy.png":"☁️", 
            "partlycloudy.png":"🌤", 
            "clear.png":"☀️",
            "fog.png": "🌫"}
    glavniy = []
    for index, latext in enumerate(links):
        text = ''
        r = requests.get(latext)
        soup = bs(r.text, "html.parser")
        
        text += soup.find("div", class_="current-day").text + "\n"
        text += soup.find("div", class_="current-forecast").img["src"].replace(" ", "")
        text += soup.find("div", class_="current-forecast").text.replace("\n", " ").replace("    ", " ") + " "
        text += soup.find("div", class_="current-forecast-desc").text + "\n"
        new = []
        if index == 0:
            for i, j, z in zip(["Утром", "Днем", "Вечером"],
                [x.img["src"] for x in soup.find_all("p", class_="icon")], 
                [x.text + "\n" for x in soup.find_all("p", class_="forecast")]):
                new.append(j)
                new.append(i)
                new.append(z)
            text += ' '.join(new)
            text += soup.find("div", class_="current-forecast-details").text.replace("\n\nВ", "\nВ").replace("\n\nЛ", "\nЛ")
            
            for word, ico in icons.items():
                text = text.replace(ico_link_ru + word, ico)
        else:
            for i, j, z in zip(["Tong", "Kun", "Oqshom"], 
                [x.img["src"] for x in soup.find_all("p", class_="icon")], 
                [x.text + "\n" for x in soup.find_all("p", class_="forecast")]):
                new.append(j)
                new.append(i)
                new.append(z)
            text += ' '.join(new)
            text += soup.find("div", class_="current-forecast-details").text.replace("\n\nN", "\nN").replace("\n\nO", "\nO")
            for word, ico in icons.items():
                text = text.replace(ico_link_uz + word, ico)
        glavniy.append(text)
    return glavniy[0], glavniy[1]

x, y = get_text(links)

def function_to_run():
    return bot.send_message(some_id, x, disable_notification=True), bot.send_message(some_id, y, disable_notification=True)


if __name__ == "__main__":
    # Create the job in schedule.
    schedule.every().day.at("03:06").do(function_to_run)
    #schedule.every(10).seconds.do(function_to_run)
   
    
    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start() 

    # And then of course, start your server.
    
