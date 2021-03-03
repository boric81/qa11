import telebot

from extensions import APIException, Converter
from config import keys, TOKEN



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message):
    intro='Для конвертации валют введите следующие данные:\n <имя конвертируемой валюты><имя необходимой валюты>' \
          '<количество>\n'\
                 'Для отображения списка валют введите команду /values'
    bot.reply_to(message, intro)

@bot.message_handler(commands=['values'])
def values(message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler (content_types=['text'])
def convert(message):
    try:
        value = message.text.split(" ")
        if len(value) != 3:
            raise APIException("Количество данных неверно")

        quote, base, amount = value
        total = Converter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f"Цена {amount} {base} в {quote} равна {total} "
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)