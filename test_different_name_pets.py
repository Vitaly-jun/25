import pytest
from selenium.webdriver.common.by import By


def test_all_pets_have_different_names(my_pets):
    '''Поверяем что на странице со списком моих питомцев, у всех питомцев разные имена'''

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Перебираем данные из pet_data
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    # Перебираем имена проверяем, если r == 0 то повторяющихся имен нет.
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_different_name_pets.py
