#!/usr/bin/python

# Это простой бот с таймером по расписанию
# https://schedule.readthedocs.io

import time, threading, schedule
from telebot import TeleBot

bot = TeleBot('7910812368:AAG-TWuPNsDie1kxQVZUUJZ9SKzfRWCZGtM')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Используйте /set <секунды>, чтобы установить таймер")


def beep(chat_id) -> None:
    """Отправляет сообщение 'Бип'."""
    bot.send_message(chat_id, text='Бип!')


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(message.chat.id)
    else:
        bot.reply_to(message, 'Использование: /set <секунды>')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)


if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
