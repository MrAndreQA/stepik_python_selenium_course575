from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/wait1.html"
    browser.get(link)

    browser.implicitly_wait(5)

    button = browser.find_element(By.ID, "verify")
    button.click()

    message = browser.find_element(By.ID, "verify_message").text

    assert "successful" in message

finally:
    time.sleep(3)
    browser.quit()