from time import sleep

import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


login = "*"
password = "*"

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_collect_corrections(browser,number):
    browser.get(f"https://stepik.org/lesson/{number}/step/1")

    # Ждём и кликаем кнопку "Войти"
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ember500"))
    ).click()

    # Ввод email
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    ).send_keys(login)

    # Ввод пароля
    browser.find_element(By.ID, "id_login_password").send_keys(password)

    # Клик по кнопке "Войти" в модальном окне
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

    # === КЛЮЧЕВОЕ ИСПРАВЛЕНИЕ ===
    wait = WebDriverWait(browser, 15)

    def find_clickable_textarea(driver):
        try:
            element = driver.find_element(By.XPATH, "//div[contains(@class, 'quiz-component')]//textarea")
            if element.is_enabled() and element.is_displayed():
                return element
            return False
        except StaleElementReferenceException:
            return False
        except:
            return False

    # Получаем **живой и кликабельный** элемент
    textarea = wait.until(find_clickable_textarea)
    answer = str(math.log(int(time.time())))
    print("ИТОГОВОЕ СООБЩЕНИЕ =", answer)
    textarea.send_keys(answer)

    # Отправляем ответ
    submit_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    submit_btn.click()

    # Проверяем результат
    success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    assert success_message.text == "Correct!", f"Ожидалось 'Correct!', но получено: '{success_message.text}'"





    """# Ждём кнопку "Войти" и кликаем
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
    #Записываю в переменную сообщение, которое не является 'Correct!' """

    """if message.text != "Correct!":
        print("Некорректное сообщение =" + message.text) """


