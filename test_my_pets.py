import pytest
from selenium.webdriver.common.by import By


def test_my_pets(my_pets):
    '''Проверяем что на странице со списком моих питомцев присутствуют все питомцы'''

    # Сохраняем в переменную элементы статистики
    num = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".table.table-hover tbody tr")

    # Получаем количество питомцев из данных статистики
    number = num[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == len(pets)
# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_my_pets.py
