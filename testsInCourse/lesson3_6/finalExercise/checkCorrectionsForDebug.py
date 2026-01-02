from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
import math


login = "*"
password = "*"


def test_collect_corrections(browser):
    browser.get("https://stepik.org/lesson/236905/step/1")

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