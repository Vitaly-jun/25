import pytest
from selenium.webdriver.common.by import By


def test_photo_pets(my_pets):
    '''Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото'''

    # Сохраняем в переменную элементы статистики
    num = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    # Сохраняем в переменную images элементы с атрибутом img
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Получаем количество питомцев из данных статистики
    number = num[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Находим половину от количества питомцев
    half_pets = number // 2

    # Находим количество питомцев с фотографией
    photo_pets = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            photo_pets += 1

    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert photo_pets >= half_pets
# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_photo_pets.py
