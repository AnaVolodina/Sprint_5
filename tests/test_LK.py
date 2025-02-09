from locators import Locators

class TestStellarBurgers:
    def test_personal_account_button(self, driver):
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

    # Проверяем url
        assert "https://stellarburgers.nomoreparties.site/account" in driver.current_url