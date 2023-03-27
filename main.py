import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

my_bot = telebot.TeleBot("6106406169:AAGwZNpsbh-ntmNfSZu1cfbFrLWMCzW3gdo") #Сюда вписать токен бота

@my_bot.message_handler(commands=["start"]) # Отслеживание команды Старт
def start(message):
    mess = f"Здравствуйте, <b>{message.from_user.first_name} {message.from_user.last_name}</b> чем могу помочь?"
    my_bot.send_message(message.chat.id, mess, parse_mode="html") #html можно изменить

@my_bot.message_handler()
def get_user_text(message):
    if message.text.lower() == "Hi":
        my_bot.send_message(message.chat.id, "И тsебе привет" , message, parse_mode="html")# Выводится вся информация из message (Нужно потом удалить)
    elif message.text.lower() == "id":
        my_bot.send_message(message.chat.id, f"Твой id:{message.from_user.id}", parse_mode="html")
    elif message.text.lower() == "photo":#Делает запрос на фото
        photo = open("maxresdefault.jpg", "rb")#Отправляю фото
        my_bot.send_photo(message.chat.id, photo)
    else:
        my_bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode="html")

#@my_bot.message_handlers(content_types = ['photo'])#Человек отправляет фото
#def get_user_photo(message):
    #my_bot.send_message((message.chat.id, "Вау, крутое фото!"))#Реакция на фото

@my_bot.message_handler(content_types = ['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт Афиши"), url ="")#Текст Кнопки и адрес ссылки
    my_bot.send_message(message.chat.id, "Официальный сайт", reply_markup=markup)

@my_bot.message_handler(content_types = ['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)#Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    website = types.KeyboardButton("Веб Сайт")
    start = types.KeyboardButton("Start")
    markup.add(website, start)#Текст Кнопки и адрес ссылки
    my_bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)

my_bot.polling(none_stop=True)