from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/cats.html"
    browser.get(link)

    #browser.implicitly_wait(5)

    browser.find_element(By.ID, "button")

finally:
    time.sleep(3)
    browser.quit()