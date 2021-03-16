from api import Petfriends


pt = Petfriends()

def test_get_api(email="", password=""):
    #запрос с пустыми полями в email и password
    status,result = pt.get_api_key(email, password)
    assert status == 403
    assert "key" not in result

def test_get_api_with_valid_user(email="test.rezebent1+3@gmail.com", password="1234567890"):
    # запрос с password из чисел
    status,result = pt.get_api_key(email, password)
    assert status == 200
    assert "key" in result


def test_get_api_with_valid_user(email="test.rezebent1+4@gmail.com", password="!@#$%^&*()[]{}?><"):
    # запрос с password из спец. символов
    status,result = pt.get_api_key(email, password)
    assert status == 200
    assert "key" in result
#
def test_get_api_with_valid_user(email="test.rezebent1+5@gmail.com", password="qwertyuiopasdfghjklzxcvbnm"):
    # запрос с password из латинских букв
    status,result = pt.get_api_key(email, password)
    assert status == 200
    assert "key" in result


def test_get_list_of_pets_with_invalid_api_key(filter=""):
    # запрос с auth_key в виде числа
    _, auth_key = pt.get_api_key("test.rezebent1+3@gmail.com", "1234567890")
    status, result = pt.get_pet_list_invalid_auth_key(auth_key, filter)
    assert status == 403
    assert "pets" not in result

def test_get_list_of_pets_with_invalid_api_key1(filter=""):
    # запрос с auth_key в виде набора спец.символов
    _, auth_key = pt.get_api_key("test.rezebent1+3@gmail.com", "1234567890")
    status, result = pt.get_pet_list_invalid_auth_key1(auth_key, filter)
    assert status == 403
    assert "pets" not in result

def test_get_list_of_pets_with_invalid_filter1(filter='%d' %(555)):
    # запрос с filter в виде числа
    _, auth_key = pt.get_api_key("test.rezebent1+3@gmail.com", "1234567890")
    status, result = pt.get_pet_list_with_invalid_filter(auth_key, filter)
    assert status == 400
    assert "pets" not in result

def test_get_list_of_pets_with_invalid_filter2(filter='pet'):
    # запрос с некорректным filter
    _, auth_key = pt.get_api_key("test.rezebent1+3@gmail.com", "1234567890")
    status, result = pt.get_pet_list_with_invalid_filter(auth_key, filter)
    assert status == 400
    assert "pets" not in result

def test_get_list_of_pets_with_uncorrect_request(filter=""):
    # запрос с put request
    _, auth_key = pt.get_api_key("test.rezebent1+3@gmail.com", "1234567890")
    status, result = pt.get_pet_list_with_put_request(auth_key, filter)
    assert status == 405
    assert "pets" not in result

def test_get_list_of_pets_with_uncorrect_request(filter=""):
    # запрос с post request
    _, auth_key = pt.get_api_key("test.rezebent1+4@gmail.com", "!@#$%^&*()[]{}?><")
    status, result = pt.get_pet_list_with_post_request(auth_key, filter)
    assert status == 405
    assert "pets" not in result




