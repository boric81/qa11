import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/Users/User/PycharmProjects/module25/tests/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.implicitly_wait(5)
    # Неявное ожидание
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    # Вводим email

    pytest.driver.find_element_by_id('email').send_keys('test.rezebent1+1@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('111111')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя


    yield

    pytest.driver.quit()

def test_images():
    """Проверка наличия фото питомцев"""
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')

    for i in range(len(images)):
        assert images[i].get_attribute('src') != ''

def test_names():
    """Проверка наличия имен питомцев"""

    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    for i in range(len(names)):
        assert names[i].text != ''

def test_pet_types():
    """Проверка наличия пород питомцев в описании"""
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')
    for i in range(len(descriptions)):
        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0


def test_pet_ages():
    """Проверка наличия возраста питомцев в описании"""

    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')
    for i in range(len(descriptions)):
        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[1]) > 0