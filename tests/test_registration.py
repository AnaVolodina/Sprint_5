from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import data
from faker import Faker

class TestStellarBurgers:
    # Генерируем случайный логин(email)
    fake = Faker()
    def fake_email(self):
        return self.fake.email()

    def test_successful_registration(self, driver):
        email = self.fake.email()
    # Открываем страницу регистрации
        driver.get(data.REGISTRATION_PAGE)

    # Заполняем поля формы
        driver.find_element(*Locators.NAME_FIELD_REGISTRATION_PAGE).send_keys(data.NAME_FOR_REGISTRATION)
        driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION_PAGE).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD_REGISTRATION_PAGE).send_keys(data.PASSWORD_FOR_LOGIN)

    # Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(*Locators.REGISTRATION_BUTTON_REGISTRATION_PAGE).click()

    # Проверяем, что регистрация прошла успешно:

    # Ждем, пока произойдет перенаправление на страницу "Вход"
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains('login'))

    # Заполняем поля на странице входа
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(data.EMAIL_FOR_LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(data.PASSWORD_FOR_LOGIN)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Ждем, пока произойдет перенаправление на главную страницу
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be(data.MAIN_PAGE))

    # Переходим в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains('profile'))

    # Проверяем, что находимся на странице личного кабинета
        assert driver.current_url == data.PERSONAL_ACCOUNT_PAGE

