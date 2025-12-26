from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    inputAnswer = browser.find_element(By.ID, "answer")
    inputAnswer.send_keys(y)

    checkBox = browser.find_element(By.ID, "robotCheckbox")
    checkBox.click()

    radioBtn = browser.find_element(By.ID, "robotsRule")
    radioBtn.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()