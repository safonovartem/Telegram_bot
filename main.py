import requests
from bs4 import BeautifulSoup as b
import telebot
from telebot import types

bot = telebot.TeleBot("6106406169:AAGwZNpsbh-ntmNfSZu1cfbFrLWMCzW3gdo") #Сюда вписать токен бота

@bot.message_handler(commands=['start']) # Отслеживание команды Старт
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
    if message.from_user.last_name == None:
        mess = f"Привет, <b>{message.from_user.first_name}</b>"
        bot.send_message(message.chat.id, mess, parse_mode="html") #html можно изменить
    elif message.from_user.first_name == None:
        mess = f"Привет,<b>{message.from_user.last_name}</b>"
        bot.send_message(message.chat.id, mess, parse_mode="html")
    else:
        mess = f"Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
        bot.send_message(message.chat.id, mess, parse_mode="html")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)  # Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    website = types.KeyboardButton("/website")
    start = types.KeyboardButton("/start")
    citys = types.KeyboardButton("/citys")
    markup.add(website, start, citys)  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Здравствуйте. Этот бот поможет вам узнать актуальные мероприятия в вашем городе", reply_markup=markup)
    bot.send_message(message.chat.id, "Вот список команд, которые вам доступны\n"
                                      "/start - Активировать бота\n"
                                      "/website - Ссылка на официальный сайт Афиши\n"
                                      "/citys - Команда для выбора вашего города", reply_markup=markup)
    bot.send_message(message.chat.id, "Выберите команду", reply_markup=markup)

@bot.message_handler(commands = ['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт Афиши", url ="https://www.afisha.ru"))#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Официальнный сайт Афиши", reply_markup=markup)

@bot.message_handler(commands = ['citys'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)#Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Tver = types.KeyboardButton("/Tver")
    Moscow = types.KeyboardButton("/Moscow")
    markup.add(Tver, Moscow)#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Выберите свой город", reply_markup=markup)

@bot.message_handler(commands = ['Tver'])
def tver_city(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)  # Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Movie = types.KeyboardButton("/Films_in_Tver")
    Concerts = types.KeyboardButton("/Сoncerts_in_Tver")
    markup.add(Movie, Concerts)  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Отлично, теперь выберите какой тип мероприятий вас интересует", reply_markup=markup)

@bot.message_handler(commands= ['Films_in_Tver'])
def films_in_tver(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши", url="https://www.afisha.ru/tver/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/tver/events/movies/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_for_films = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_for_films]

    Text_for_films = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще', '«Афиша» в соц. сетях', 'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время', 'Рассылка «Афиши»: главные события недели — у вас на почте']
    if Text_for_films in Trach_words:
        del Text_for_films[Text_for_films.index(Trach_words)]

    for i in Text_for_films:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это фильмы, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть трейлер прямо на сайте Афиши",reply_markup=markup)  # Возможно эту строку надо перенести в конец

@bot.message_handler(commands= ['Сoncerts_in_Tver'])
def films_in_tver(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши", url="https://www.afisha.ru/tver/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/tver/events/concerts/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_for_concerts = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_for_concerts]

    Text_for_concerts = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще', '«Афиша» в соц. сетях', 'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время', 'Рассылка «Афиши»: главные события недели — у вас на почте']
    if Text_for_concerts in Trach_words:
        del Text_for_concerts[Text_for_concerts.index(Trach_words)]

    for i in Text_for_concerts:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это концерты, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть описание прямо на сайте Афиши", reply_markup=markup)  # Возможно эту строку надо перенести в конец

@bot.message_handler()
def get_user_text(message):
    #bot.send_message(message.chat.id, message, parse_mode="html")
    if message.text.lower == "Привет" or "Hi" or "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode="html")
    elif message.text.lower == "id":# Выводится вся информация из message (Нужно потом удалить)
        bot.send_message(message.chat.id, f"Твой id:{message.from_user.id}", parse_mode="html")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode="html")

bot.polling(none_stop=True)
