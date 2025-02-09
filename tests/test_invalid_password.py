from locators import Locators

class TestStellarBurgers:
    def test_error_invalid_password(self, driver):
    # Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()

    # Заполняем поля формы на странице входа

        valid_email = "anastasiyavolodina15000@mail.ru"  # корректный email
        invalid_password = "12345"  # некорректный пароль

        driver.find_element(*Locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(invalid_password)

    # Нажимаем на кнопку "Войти" на странице входа
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Проверяем, что появилось сообщение об ошибке "Некорректный пароль"
        error_message = driver.find_element(*Locators.ERROR_MESSAGE)
        assert error_message.text == "Некорректный пароль"
