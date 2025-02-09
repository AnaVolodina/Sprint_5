from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestStellarBurgers:
    def test_constructor_button(self, driver):
    # Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()

    # Заполняем поля формы на странице входа
        valid_email = "anastasiyavolodina15000@mail.ru"  # корректный email
        valid_password = "123456"  # корректный пароль

        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(valid_password)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Переходим в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/account"))

    # Нажимаем на кнопку "Конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    # Проверяем url
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_logo_button(self, driver):
    # Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()

    # Заполняем поля формы на странице входа
        valid_email = "anastasiyavolodina15000@mail.ru"  # корректный email
        valid_password = "123456"  # корректный пароль

        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(valid_password)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Переходим в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/account"))

    # Нажимаем на логотип Stellar Burgers
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS).click()

    # Проверяем url
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'