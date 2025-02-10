from locators import Locators
import data

class TestStellarBurgers:
    def test_error_invalid_password(self, driver):
    # Открываем главную страницу
        driver.get(data.MAIN_PAGE)

    # Нажимаем на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()

    # Заполняем поля формы на странице входа
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(data.EMAIL_FOR_LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(data.INVALID_PASSWORD)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Проверяем, что появилось сообщение об ошибке "Некорректный пароль"
        error_message = driver.find_element(*Locators.ERROR_MESSAGE)
        assert error_message.text == "Некорректный пароль"
