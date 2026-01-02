import math
from time import time
import pytest
from selene import browser, be, have, by


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.driver_name = "chrome"
    browser.config.base_url = "https://stepik.org"
    browser.config.timeout = 30.0  # Увеличили таймаут
    yield
    browser.quit()


login = "*"
password = "*"


@pytest.mark.parametrize('lesson_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_collect_corrections_with_selene(lesson_id):
    # Открываем урок
    browser.open(f"/lesson/{lesson_id}/step/1")

    # Кликаем "Log in" — по тексту или стабильному селектору
    browser.element("#ember500").should(be.visible.and_(be.clickable)).click()

    # Вводим логин и пароль
    browser.element("#id_login_email").should(be.visible).type(login)
    browser.element("#id_login_password").type(password)
    browser.element("//button[@type='submit']").click()

    # Ждём, что мы на нужной странице
    browser.should(have.url_containing(f"/lesson/{lesson_id}/step/1"))

    # Ждём загрузки компонента квиза
    browser.element(".quiz-component").should(be.visible)

    # Ищем textarea
    textarea = browser.element(by.xpath("//div[contains(@class, 'quiz-component')]//textarea"))
    #textarea.should(be.enabled.and_(be.visible))

    # Вычисляем и отправляем ответ
    answer = str(math.log(int(time())))
    print("ИТОГОВОЕ СООБЩЕНИЕ =", answer)
    textarea.type(answer)

    # Отправляем решение
    browser.element(".submit-submission").should(be.clickable).click()

    # Проверяем, что появилось сообщение "Correct!"
    browser.element(".smart-hints__hint").should(have.text("Correct!"), timeout=30)