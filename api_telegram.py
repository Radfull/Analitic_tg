import telebot
from telebot import *
from api_requests import *
from graph import *

TOKEN = "6754968170:AAGE0C8AJROnSKr9YLrJUyZqPTqGnR8NrDQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("\U0001F535 YoBit.Net")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Здравствуйте! Добро пожаловать. Меня зовут Люциус.\n\nВыберите Биржу \U00002935", reply_markup=markup)


@bot.message_handler(content_types='text')
def market(message):
     if message.text == "\U0001F535 YoBit.Net":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("\U0001F4CA Аналитика")
        btn2 = types.KeyboardButton("\U00002699 Настройки")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Выберите действие \U00002935", reply_markup=markup)
        bot.register_next_step_handler(message , menu)


@bot.message_handler(content_types='text')
def menu(message):
    if message.text == "\U0001F4CA Аналитика":
        bot.send_message(message.from_user.id, "Введите криптовалюту (например btc)")
        bot.register_next_step_handler(message , user_text)
        
    if message.text == "\U00002699 Настройки":
        bot.send_message(message.from_user.id, "Данный раздел в разработке...")
        bot.register_next_step_handler(message , menu)

def user_text(message):
    data = message.text.split()
    ticker = get_ticker(data[0])
    trades = get_trades(data[0])
    data_graph(data[0])
    bot.send_photo(message.from_user.id, photo=open(f'graphs/{data[0]}_usd.png', 'rb'))
    bot.send_message(message.from_user.id, f" Успешно!\n\n Ваша пара: {data[0]}_usd\n\nИнформация:\nСредняя цена (за 24 часа): {ticker[0]} $\nОбъем торгов (за 24 часа): {ticker[1]} $\nСумма {data[0]} на продажу: {trades[0]} $\nСумма {data[0]} на покупку: {trades[1]} $\n\n Мнение ChatGPT о паре:\n")
    data_graph_delete(data[0])
    bot.register_next_step_handler(message , menu)

bot.infinity_polling()
