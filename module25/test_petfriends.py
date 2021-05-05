import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/Users/User/PycharmProjects/module25/tests/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    # Вводим email

    pytest.driver.find_element_by_id('email').send_keys('test.rezebent1+1@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('111111')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    pytest.driver.find_element_by_xpath('//a[@href="/my_pets"]').click()


    yield

    pytest.driver.quit()


def test_all_my_pets_in_table():
    """"проверка, что на странице со списком питомцев пользователя
     присутствуют все питомцы"""
    element=WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located(('id','navbarNav')))
    # Явное ожидание
    images = pytest.driver.find_elements_by_css_selector('th>img')
    # поиск фото питомцев
    title=pytest.driver.find_element_by_xpath('//*[h2][1]').text.split()
    #title=pytest.driver.find_element_by_xpath('//*[contains(text(),"Питомцев")]').text.split()
    # поиск количества питомцев в заголовке

    assert title[2]==str(len(images))


def test_half_pets_get_photo():
    """"проверка, что на странице со списком питомцев пользователя
         у половины питомцев есть фото"""
    images = pytest.driver.find_elements_by_css_selector('th>img')
    for i in range(len(images)//2):
        assert images[i].get_attribute('src') != ''
    # проверка наличия фото хотя бы у половины питомцев

def test_all_pets_have_descriptions():
    """"проверка, что на странице со списком питомцев пользователя
             у всех питомцев есть имя, возраст и порода"""

    names = pytest.driver.find_elements_by_xpath('//td[1]')
    pet_types = pytest.driver.find_elements_by_xpath('//td[2]')
    ages = pytest.driver.find_elements_by_xpath('//td[3]')
    for i in range(len(names)):
        assert names[i].text !=''
        assert pet_types[i].text !=''
        assert ages[i].text !=''

def test_no_repeat_names():
    """"проверка, что на странице со списком питомцев пользователя
                 у всех питомцев разные имена"""
    names = pytest.driver.find_elements_by_xpath('//td[1]')
    

