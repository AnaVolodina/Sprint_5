from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestStellarBurgers:
    def test_login_button_in_main_page(self, driver):
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

    # Нажимаем на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/account"))
    # Проверяем url
        assert "https://stellarburgers.nomoreparties.site/account" in driver.current_url


    def test_login_by_lk_button(self, driver):
    # Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    # Заполняем поля формы на странице входа
        valid_email = "anastasiyavolodina15000@mail.ru"  # корректный email
        valid_password = "123456"  # корректный пароль

        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(valid_password)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Нажимаем на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/account"))
    # Проверяем url
        assert "https://stellarburgers.nomoreparties.site/account" in driver.current_url


    def test_login_by_button_in_registration_form(self, driver):
    # Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()

    # Нажимаем на кнопку "Зарегистрироваться" на странице входа

        driver.find_element(*Locators.REGISTRATION_BUTTON_LOGIN_PAGE).click()

    # Нажимаем на кнопку "Войти" на странице регистрации
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_PAGE).click()

    # Заполняем поля формы на странице входа
        valid_email = "anastasiyavolodina15000@mail.ru"  # корректный email
        valid_password = "123456"  # корректный пароль

        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(valid_password)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Нажимаем на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/account"))

    # Проверяем url
        assert "https://stellarburgers.nomoreparties.site/account" in driver.current_url

    def test_login_button_forgot_password_page(self, driver):
    # Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()

    # Нажимаем на кнопку "Восстановить пароль"
        driver.find_element(*Locators.FORGOT_PASSWORD_BUTTON).click()

    # Нажимаем на кнопку "Войти" на странице восстановления пароля
        driver.find_element(*Locators.LOGIN_BUTTON_FORGOT_PASSWORD_PAGE).click()

    # Заполняем поля формы на странице входа
        valid_email = "anastasiyavolodina15000@mail.ru"  # корректный email
        valid_password = "123456"  # корректный пароль

        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(valid_password)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Нажимаем на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/account"))

    # Проверяем url
        assert "https://stellarburgers.nomoreparties.site/account" in driver.current_url