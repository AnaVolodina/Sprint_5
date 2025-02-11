from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import data

class TestStellarBurgers:
    def test_logout_button(self, driver):
    # Открываем главную страницу
        driver.get(data.MAIN_PAGE)

    # Нажимаем на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()

    # Заполняем поля формы на странице входа
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(data.EMAIL_FOR_LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(data.PASSWORD_FOR_LOGIN)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Переходим в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains('profile'))
    # Нажимаем на кнопку "Выход"
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (Locators.LOGIN_BUTTON))
        )

    # Проверяем url
        assert driver.current_url == data.LOGIN_PAGE
