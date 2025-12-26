from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    firstName = browser.find_element(By.NAME, "firstname")
    firstName.send_keys("Ivan")

    lastName = browser.find_element(By.NAME, "lastname")
    lastName.send_keys("Petrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("123@mail.ru")

    # Получаем путь к текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "testQA.txt")

    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()