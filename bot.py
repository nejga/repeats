# coding: utf8
import telebot
from config import TOKEN, ADMIN
from db import tgidregister, countusers

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        'Привет, я простой эхо бот, меня создал ChatGPT, напиши мне что-нибудь и я пришлю тебе это в ответ.\n\n'
        'Рекомендую подписаться на канал <a href="https://t.me/ChatGPTcrtd">ChatGPT создал</a>',
        parse_mode='HTML'
    )
    tgidregister(message.chat.id)

@bot.message_handler(commands=['stat'])
def stat_handler(message):
    if message.chat.id == ADMIN:
        bot.send_message(ADMIN, f'Статистика:\nКоличество пользователей: {countusers()}')
    else:
        bot.send_message(message.chat.id, message.text)

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling(interval=0)
