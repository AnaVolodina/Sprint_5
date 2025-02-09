from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestStellarBurgers:
    def test_successful_registration(self, driver):
    # Открываем страницу регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполняем поля формы
        driver.find_element(*Locators.NAME_FIELD_REGISTRATION_PAGE)
        driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION_PAGE)
        driver.find_element(*Locators.PASSWORD_FIELD_REGISTRATION_PAGE)

        valid_name = "Anastasiya" #корректное имя
        valid_email = "anastasiyavolodina15567@mail.ru" #корректный email
        valid_password = "123456" #корректный пароль

        driver.find_element(*Locators.NAME_FIELD_REGISTRATION_PAGE).send_keys(valid_name)
        driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION_PAGE).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_FIELD_REGISTRATION_PAGE).send_keys(valid_password)

    # Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(*Locators.REGISTRATION_BUTTON_REGISTRATION_PAGE).click()

    # Проверяем, что регистрация прошла успешно

    # Ждем, пока произойдет перенаправление на страницу "Вход"
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/login"))

    # Заполняем поля на странице входа
        valid_email = "anastasiyavolodina15000@mail.ru"  # корректный email
        valid_password = "123456"  # корректный пароль

        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(valid_password)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Ждем, пока произойдет перенаправление на главную страницу
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/"))

    # Переходим в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    # Проверяем, что находимся на странице личного кабинета
        assert "https://stellarburgers.nomoreparties.site/account" in driver.current_url

