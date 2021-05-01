import telebot
import argparse
import os

parser = argparse.ArgumentParser(description='Отправка сообщения в телеграм, для установки параметров отправки используются переменные среды TELEGRAM_API_KEY и CHAT_ID ver 0.1 ')

parser.add_argument('--file', default='NONE', help='Пусть к файлу для отправки (не более 5 mb)')
parser.add_argument('--message', default='NONE', help='Текст сообщения для отправки (используется только разметка default') 
parser.add_argument('--photo', default='NONE', help='Путь к фото для отправки (не более 15 mb)')

args = parser.parse_args()

API_KEY = os.environ.get('TELEGRAM_API_KEY')
CHAT_ID = os.environ.get('CHAT_ID')
if API_KEY == "None" or CHAT_ID == "None":
    print("Необходимо задать токен для вашего бота -  set (export) TELEGRAM_API_KEY=API-KEY и указать CHAT_ID  - export CHAT_ID=Chat-ID")
bot = telebot.TeleBot(API_KEY) # You can set parse_mode by default. HTML or MARKDOWN

if args.message == "NONE" and args.file == "NONE" and args.photo == "NONE":
    print("Должен быть хотя бы один аргумент, для более подробной справки запустите программу с ключем --help")
if args.message != "NONE":
    bot.send_message(CHAT_ID, args.message)
if args.file !="NONE":
    if os.path.exists(args.file):
        if os.path.getsize(args.file) > 5000000:
            print("too big size (5 mb or more)")
        else:
            doc = open(args.file, 'rb')
            bot.send_document(CHAT_ID, doc)
    else:
        print('Нет такого файла') # False

if args.photo !="NONE":
    if os.path.exists(args.photo):
        if os.path.getsize(args.photo) > 15000000:
            print("too big size (15 mb or more)")
        else:
            doc = open(args.photo, 'rb')
            bot.send_photo(CHAT_ID, doc)
    else:
        print('Нет такого файла c фото') # False



