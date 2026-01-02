from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

fake = Faker()
word = fake.word()

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


"""для генерации рандомных данных можно использовать библиотеку Faker
from faker import Faker
чтобы занести данные в переменную используйте такую конструкцию:

fake = Faker()
word = fake.word()

Вот список некоторых типов данных, которые можно генерировать с помощью библиотеки Faker в Python:

Имя: fake.name()
Адрес: fake.address()
Текст: fake.text()
Случайное число: fake.random_number()
Электронная почта: fake.email()
Телефонный номер: fake.phone_number()
Дата: fake.date()
Время: fake.time()
URL: fake.url()
Пароль: fake.password()
Пользовательское слово: fake.word()
Пользовательская фраза: fake.sentence()
Пользовательский абзац: fake.paragraph()
Идентификатор: fake.uuid4()
Валюта: fake.currency()
Компания: fake.company()
Профессия: fake.job()
Источник: fake.bs()
Цвет: fake.color_name()
Почтовый индекс: fake.postcode() """