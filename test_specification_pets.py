import pytest
from selenium.webdriver.common.by import By


def test_there_is_a_name_age_and_gender(my_pets):
    '''Поверяем что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода'''

    # Сохраняем элементы с данными о питомцах
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    name = []
    animal = []
    age = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        name.append(split_data_pet[0])
        animal.append(split_data_pet[1])
        age.append(split_data_pet[2])
    # Проверяем полученные данные
    for i in range(len(name)):
        assert name[i] != ''
        assert animal[i] != ''
        assert age[i] != ''
# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test_specification_pets.py
