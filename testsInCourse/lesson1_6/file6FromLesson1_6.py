from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    inputFirstName = browser.find_element(By.XPATH, "//div[@class='first_block']/div[1]/input")
    inputFirstName.send_keys("Ivan")

    inputLastName = browser.find_element(By.XPATH, "//div[@class='first_block']/div[2]/input")
    inputLastName.send_keys("Petrov")

    inputEmail = browser.find_element(By.XPATH, "//div[@class='first_block']/div[3]/input")
    inputEmail.send_keys("sema@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()