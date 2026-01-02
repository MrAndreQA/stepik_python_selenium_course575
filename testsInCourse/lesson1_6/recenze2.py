from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def main():
    try:
        link = "https://suninjuly.github.io/registration2.html"
        req = False

        driver = webdriver.Chrome()
        driver.get(link)
        wait = WebDriverWait(driver, 90)
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        fname_field = driver.find_element(By.XPATH, '//input[contains(@placeholder,"first name")]')
        fname_field.send_keys("Ivan")

        lname_field = driver.find_element(By.XPATH, '//input[contains(@placeholder,"last name")]')
        lname_field.send_keys("Petrov")

        email_field = driver.find_element(By.XPATH, '//input[contains(@placeholder,"email")]')
        email_field.send_keys("ivan@petrov.com")

        if not req:
            phone_field = driver.find_element(By.XPATH, '//input[contains(@placeholder,"phone")]')
            phone_field.send_keys("88005553535")

            address_field = driver.find_element(By.XPATH, '//input[contains(@placeholder,"address")]')
            address_field.send_keys("Lenina, 1")

        confirm_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        confirm_button.click()
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        welcome_text_el = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_el.text

        assert "Congratulations! You have successfully registered!" == welcome_text


    finally:
        sleep(5)
        driver.quit()


if __name__ == '__main__':
    main()
