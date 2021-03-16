import requests
import json


class Petfriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email: str, password: str) ->json:
        """Метод отправляет запрос с email и паролем пользвателя к API сервера,
         чтобы получить авторизационный ключ в формате JSON и статус запроса"""
        headers={
            "email": email,
            "password": password
        }
        res=requests.get(self.base_url+"api/key",headers=headers)
        status=res.status_code
        result = ""
        try:
            result = res.json()
        except :
            result = res.text
        return status, result

    def get_pet_list_invalid_auth_key(self,auth_key:json,filter) -> json:
        """Метод отправляет запрос с ключом пользователя в виде числа и фильтром к API сервера,
          чтобы получить список питомцев и статус запроса"""
        headers={'auth_key':'%d' %(545)} # auth_key в виде числа
        filter={'filter': filter}
        res=requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_pet_list_invalid_auth_key1(self,auth_key:json,filter) -> json:
        """Метод отправляет запрос с ключом пользователя в виде набора символов и фильтром к API сервера,
          чтобы получить список питомцев и статус запроса"""
        headers={'auth_key': '@#%^'} # auth_key в виде набора спец.символов
        filter={'filter': filter}
        res=requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_pet_list_with_invalid_filter(self,auth_key:json,filter) -> json:
        """Метод отправляет запрос с ключом пользователя в виде числа и фильтром к API сервера,
          чтобы получить список питомцев и статус запроса"""
        headers={'auth_key':auth_key['key']} # auth_key в виде числа
        filter={'filter': filter}
        res=requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_pet_list_with_put_request(self,auth_key:json,filter) -> json:
        """Метод отправляет put запрос с уникальным ключом пользователя и фильтром к API сервера,
          чтобы получить список питомцев и статус запроса"""
        headers={'auth_key': auth_key['key']}
        filter={'filter':filter}
        res=requests.put(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_pet_list_with_post_request(self,auth_key:json,filter) -> json:
        """Метод отправляет post запрос с уникальным ключом пользователя и фильтром к API сервера,
          чтобы получить список питомцев и статус запроса"""
        headers={'auth_key': auth_key['key']}
        filter={'filter':filter}
        res=requests.post(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result






