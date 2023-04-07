import requests
from bs4 import BeautifulSoup
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
    bot.send_message(message.chat.id, "Выберите команду", reply_markup=markup)

@bot.message_handler(commands = ['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт Афиши", url ="https://www.afisha.ru"))#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Официальнный сайт Афиши", reply_markup=markup)

@bot.message_handler(commands = ['citys'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 20)#Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Tver = types.KeyboardButton("/Tver")
    Moscow = types.KeyboardButton("/Moscow")
    Saint_Petersburg = types.KeyboardButton("/Saint-Petersburg")
    Nizhny_Novgorod = types.KeyboardButton("/Nizhny_Novgorod")
    Novorossiysk = types.KeyboardButton("/Novorossiysk")
    Bryansk = types.KeyboardButton("/Bryansk")
    Rostov_on_don = types.KeyboardButton("/Rostov-on-don")
    Voronezh = types.KeyboardButton("/Voronezh")
    Saint_Petersburg = types.KeyboardButton("/Saint-Petersburg")
    Nizhny_Novgorod = types.KeyboardButton("/Nizhny_Novgorod")
    Novorossiysk = types.KeyboardButton("/Novorossiysk")
    Bryansk = types.KeyboardButton("/Bryansk")
    Velikiy_Novgorod = types.KeyboardButton("/Velikiy_Novgorod")

    markup.add(Tver, Moscow, Saint_Petersburg, Nizhny_Novgorod, Novorossiysk, Bryansk, Velikiy_Novgorod)#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Выберите свой город", reply_markup=markup)

@bot.message_handler(commands = ["/Tver"])
def tver_city(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт Афиши", url="https://www.afisha.ru"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Официальнный сайт Афиши", reply_markup=markup)

@bot.message_handler(commands=["/Tver"])
    def tver_city(message):

        Moscow = types.KeyboardButton("/Moscow")
    Saint_Petersburg = types.KeyboardButton("/Saint-Petersburg")
    Nizhny_Novgorod = types.KeyboardButton("/Nizhny_Novgorod")
    Novorossiysk = types.KeyboardButton("/Novorossiysk")
    Bryansk = types.KeyboardButton("/Bryansk")
    Rostov_on_don = types.KeyboardButton("/Rostov-on-don")
    Voronezh = types.KeyboardButton("/Voronezh")
    Saint_Petersburg = types.KeyboardButton("/Saint-Petersburg")
    Nizhny_Novgorod = types.KeyboardButton("/Nizhny_Novgorod")
    Novorossiysk = types.KeyboardButton("/Novorossiysk")
    Bryansk = types.KeyboardButton("/Bryansk")
    Velikiy_Novgorod = types.KeyboardButton("/Velikiy_Novgorod")

    markup.add(Tver, Moscow, Saint_Petersburg, Nizhny_Novgorod, Novorossiysk, Bryansk, Velikiy_Novgorod)#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Выберите свой город", reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    #bot.send_message(message.chat.id, message, parse_mode="html")
    if message.text.lower == "Привет" or "Hi" or "Hello":
        bot.send_message(message.chat.id, "И тебе привет" ,parse_mode="html")# Выводится вся информация из message (Нужно потом удалить)
    elif message.text.lower == "id":
        bot.send_message(message.chat.id, f"Твой id:{message.from_user.id}", parse_mode="html")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode="html")

bot.polling(none_stop=True)
