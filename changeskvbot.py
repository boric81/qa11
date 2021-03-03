import telebot
import requests
import json

TOKEN = "1404223753:AAE3EJYMrJ-dzQtXUAEZHbDnFJLEJ2qlWSA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message):
    intro='Для конвертации валют введите следующие данные:\n <имя конвертируемой валюты><имя необходимой валюты>' \
          '<количество>\n'\
                 'Для отображения списка валют введите команду /values'
    bot.reply_to(message, intro)

keys = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'фунт': "GBP"
}

class ConvertException (Exception):
    pass

@bot.message_handler(commands=['values'])
def values(message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler (content_types=['text'])
def get_price(message):
    values = message.text.split(" ")

    quote, base, amount = values

    r = requests.get(f'https://api.exchangeratesapi.io/latest?symbols={keys[quote]}')
    answer = json.loads(r.content)
    curs = answer.get("rates")
    curs_skv = curs.get(keys[quote])
    a=int(amount)
    total = curs_skv*a
    text = f"Цена {amount} {base} в {quote} равна {total} "
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)