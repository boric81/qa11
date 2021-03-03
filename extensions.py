
import requests
import json
from config import keys


class APIException (Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f"Невозможно конвертировать в {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Невозможно конвертировать количество {amount}")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException (f"Невозможно конвертировать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException (f"Невозможно конвертировать валюту {base}")

        r = requests.get(f'https://api.exchangeratesapi.io/latest?symbols={keys[quote]}')
        answer = json.loads(r.content)
        curs = answer.get("rates")
        curs_skv = curs.get(keys[quote])
        a = int(amount)
        total = curs_skv * a

        return total