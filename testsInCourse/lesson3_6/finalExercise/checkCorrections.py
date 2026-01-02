from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


login = "*"
password = "*"

def test_collect_corrections(browser):
    browser.get("https://stepik.org/lesson/236895/step/1")

    # Ждём кнопку "Войти" и кликаем
    login_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ember500"))
    )
    login_btn.click()


    # Ввод email
    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    )
    email_input.send_keys(login)

    # Ввод пароля
    pwd_input = browser.find_element(By.ID, "id_login_password")
    pwd_input.send_keys(password)

    # Клик по кнопке "Войти" в модальном окне
    submit_btn = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_btn.click()

    # Ждём появления текстового поля для ввода ответа и вводим его
    wait = WebDriverWait(browser, 15)
    textarea = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='show-plugin']//textarea")))
    textarea.click()
    textarea.clear()
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))



    #Отправляем решение
    submit_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    submit_btn.click()



    # Ждём сообщение
    success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    assert success_message.text == "Correct!", f"Ожидалось 'Correct!', но получено: '{success_message.text}'"
    #Записываю в переменную сообщение, которое не является 'Correct!'

    """if message.text != "Correct!":
        print("Некорректное сообщение =" + message.text) """


