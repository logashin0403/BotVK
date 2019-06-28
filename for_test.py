import vk_api.vk_api
from vk_api.bot_longpoll import VkBotEventType
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
import time
from threading import Thread
import threading
import sys
import requests
from bs4 import BeautifulSoup

class Bot:

    def __init__(self):

        #API
        self.token = "9604fbd6d224d3709b72a06bd3be67b8dae737dded070d094129c175ab2cc7d4810ec88b7eed1056bea2b"
        self.gid = 181971637
        self.vk = vk_api.VkApi(token = self.token)
        self.long_poll = VkBotLongPoll(self.vk, self.gid, wait = 30)
        self.vk_api = self.vk.get_api()
        keyboard = VkKeyboard(one_time=False)
        #API
        #Helps
        self.golod = 100
        self.sleepp = 100
        self.toi = 100
        self.ev_us_id = 0
        self.ran_us_id = 0
        #Helps
        #funs
        self.html_doc = requests.get('https://randstuff.ru/joke/')
        self.app = BeautifulSoup(self.html_doc.text, "html.parser")
        self.res1 = ((self.app.select('.text')[0].getText()))
        #funs
        #fancts
        self.html_docc = requests.get('https://randstuff.ru/fact/')
        self.app = BeautifulSoup(self.html_docc.text, "html.parser")
        self.res2 = ((self.app.select('.text')[0].getText()))
        #facts
        #weather
        self.start_url = 'https://pogoda.mail.ru/prognoz/'
        self.city_user = ''
        self.city_user2 = ''
        #weather
        #fancts
        if __name__ == '__main__':
            Thread(target = self.startbot).start()
            Thread(target = self.minus).start()
        #fancts

        #minushelps
    def minus(self):

        while True:
            self.golod = self.golod - 0.01
            self.golod = round(self.golod, 2)
            self.sleepp = self.sleepp - 0.01
            self.sleepp = round(self.sleepp, 2)
            self.toi = self.toi - 0.01
            self.toi = round(self.toi, 2)
            time.sleep(3)
            print(self.golod, self.toi, self.sleepp)
        #minushelps
    def weather_info(self):

        self.city_user = self.city_user.lower()
        self.city_user2 = self.city_user
        self.city_user = self.city_user.replace('ь', '')
        self.city_user = self.city_user.replace('ъ', '')
        self.city_user = self.city_user.replace('а', 'a')
        self.city_user = self.city_user.replace('б', 'b')
        self.city_user = self.city_user.replace('в', 'v')
        self.city_user = self.city_user.replace('г', 'g')
        self.city_user = self.city_user.replace('д', 'd')
        self.city_user = self.city_user.replace('е', 'e')
        self.city_user = self.city_user.replace('ж', 'zh')
        self.city_user = self.city_user.replace('з', 'z')
        self.city_user = self.city_user.replace('и', 'i')
        self.city_user = self.city_user.replace('й', 'y')
        self.city_user = self.city_user.replace('к', 'k')
        self.city_user = self.city_user.replace('л', 'l')
        self.city_user = self.city_user.replace('м', 'm')
        self.city_user = self.city_user.replace('н', 'n')
        self.city_user = self.city_user.replace('о', 'o')
        self.city_user = self.city_user.replace('п', 'p')
        self.city_user = self.city_user.replace('р', 'r')
        self.city_user = self.city_user.replace('с', 's')
        self.city_user = self.city_user.replace('т', 't')
        self.city_user = self.city_user.replace('у', 'u')
        self.city_user = self.city_user.replace('ф', 'f')
        self.city_user = self.city_user.replace('х', 'h')
        self.city_user = self.city_user.replace('ц', 'ts')
        self.city_user = self.city_user.replace('ч', 'ch')
        self.city_user = self.city_user.replace('ш', 'sh')
        self.city_user = self.city_user.replace('щ', 'sche')
        self.city_user = self.city_user.replace('ы', 'i')
        self.city_user = self.city_user.replace('э', 'e')
        self.city_user = self.city_user.replace('ю', 'yu')
        self.city_user = self.city_user.replace('я', 'ya')
        self.city_user = self.city_user.replace(' ', '_')
        if self.city_user2 == "санкт-петербург":
            self.city_user = self.city_user.replace('-', '_')
        try:
            self.start_url = self.start_url + self.city_user + '/'
            self.html_doc3 = requests.get(self.start_url)
            self.app = BeautifulSoup(self.html_doc3.text, "html.parser")
            self.res4 = ((self.app.select('.information__content__temperature')[0].getText()))
            self.vk_api.messages.send(peer_id = self.ev_us_id, random_id = self.ran_us_id, message = self.res4)
        except:
            self.vk_api.messages.send(peer_id = self.ev_us_id, random_id = self.ran_us_id, message = "Город написан не правильно или его не существует")
        #wether_info

        #keyboard
    def create_keyboard(self):

        print(self.response)
        keyboard = VkKeyboard(one_time=False)
        if self.response != " ":
            keyboard.add_button('информация о животном', color=VkKeyboardColor.POSITIVE)
            keyboard.add_button('покормить', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('уложить спать', color=VkKeyboardColor.POSITIVE)
            keyboard.add_button('сводить в туалет', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('шуточка', color=VkKeyboardColor.POSITIVE)
            keyboard.add_button('факт', color=VkKeyboardColor.POSITIVE)
            keyboard.add_button('погода', color=VkKeyboardColor.POSITIVE)

        keyboard = keyboard.get_keyboard()
        return keyboard
        #keyboard


    def startbot(self):
        print("server is activated")
        for event in self.long_poll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.response = event.object.text.lower()
                keyboard = self.create_keyboard()
                self.ev_us_id = event.object.peer_id
                self.ran_us_id = event.object.random_id
                if self.response == "информация о животном":
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = f"Уровень голода: {self.golod}\n Уровень туалета: {self.toi}\n Уровень сна: {self.sleepp}", keyboard = keyboard)
                elif self.response == "покормить":
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = "Спасибо, было вкусно!", keyboard = keyboard)
                    self.golod = 100
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = f"Уровень голода: {self.golod}\n Уровень туалета: {self.toi}\n Уровень сна: {self.sleepp}", keyboard = keyboard)
                elif self.response == "уложить спать":
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = "Я отлично поспал!", keyboard = keyboard)
                    self.sleepp = 100
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = f"Уровень голода: {self.golod}\n Уровень туалета: {self.toi}\n Уровень сна: {self.sleepp}", keyboard = keyboard)
                elif self.response == "сводить в туалет":
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = "Сколько во мне было гадостей", keyboard = keyboard)
                    self.toi = 100
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = f"Уровень голода: {self.golod}\n Уровень туалета: {self.toi}\n Уровень сна: {self.sleepp}", keyboard = keyboard)
                elif self.response == "шуточка":
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = self.res1, keyboard = keyboard)
                    self.html_doc = requests.get('https://randstuff.ru/joke/')
                    self.app = BeautifulSoup(self.html_doc.text, "html.parser")
                    self.res1 = ((self.app.select('.text')[0].getText()))
                elif self.response == "факт":
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = self.res2, keyboard = keyboard)
                    self.html_docc = requests.get('https://randstuff.ru/fact/')
                    self.app = BeautifulSoup(self.html_docc.text, "html.parser")
                    self.res2 = ((self.app.select('.text')[0].getText()))
                elif self.response == "погода":
                    try:
                        self.city_user = self.vk_api.users.get(user_id = event.object.from_id, fields = "city")[0]["city"]["title"]
                    except:
                        self.city_user = "Moscow"
                    self.weather_info()
                else:
                    self.vk_api.messages.send(peer_id = event.object.peer_id, random_id = event.object.random_id, message = "Извини, но я не понял тебя(")

bot = Bot()
