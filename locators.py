import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators():
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, '//button[text()="Войти в аккаунт"]') #кнопка "Войти в аккаунт" на главной странице
    NAME_FIELD_REGISTRATION_PAGE = (By.XPATH, '//label[text()="Имя"]/following-sibling::input') #поле "Имя" на странице регистрации
    EMAIL_FIELD_REGISTRATION_PAGE = (By.XPATH, '//label[text()="Email"]/following-sibling::input') #поле "Email" на странице регистрации
    PASSWORD_FIELD_REGISTRATION_PAGE = (By.NAME, 'Пароль') #поле "Пароль" на странице регистрации
    REGISTRATION_BUTTON_REGISTRATION_PAGE = (By.XPATH, '//button[text()="Зарегистрироваться"]') # кнопка "Зарегистрироваться" на странице регистрации
    EMAIL_FIELD_LOGIN_PAGE = (By.XPATH, "//input[@type='text']")  #поле "Email" на странице входа
    PASSWORD_FIELD_LOGIN_PAGE = (By.XPATH, ".//input[@type='password']") #поле "Пароль" на странице входа
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')   #кнопка "Войти" на странице входа
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]') #кнопка "Личный кабинет"
    REGISTRATION_BUTTON_LOGIN_PAGE = (By.XPATH, '//a[contains(text(), "Зарегистрироваться")]') # кнопка "Зарегистрироваться" на странице входа
    LOGIN_BUTTON_REGISTRATION_PAGE = (By.XPATH, '//a[contains(text(), "Войти")]') # кнопка "Войти" на странице регистрации
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[contains(text(), "Восстановить пароль")]') #кнопка "Восстановить пароль"
    LOGIN_BUTTON_FORGOT_PASSWORD_PAGE = (By.XPATH, '//a[contains(text(), "Войти")]') #кнопка "Войти" на странице восстановления пароля
    ERROR_MESSAGE = (By.XPATH, '//p[text()="Некорректный пароль"]') #сообщение об ошибке "Некорректный пароль" на странице входа
    LOGOUT_BUTTON = (By.XPATH, "//li[@class='Account_listItem__35dAP']//button[contains(text(), 'Выход')]") #кнопка "Выход" в личном кабинете
    LOGO_STELLAR_BURGERS = (By.XPATH, '//div/a[@href="/"]') #логотип STELLAR_BURGERS
    CONSTRUCTOR_BUTTON = (By.XPATH, '//li/a[@href="/"]') #кнопка "Конструктор"
    BURGER_INGREDIENTS_CONTAINER = (By.CSS_SELECTOR, "section.BurgerIngredients_ingredients__1N8v2") # Контейнер с ингредиентами
    HEADER_SAUCES = (By.XPATH, "//h2[text()='Соусы']") # Заголовок раздела "Соусы"
    HEADER_FILLINGS = (By.XPATH, '//h2[text()="Начинки"]') # Заголовок раздела "Начинки"
    HEADER_BUNS = (By.XPATH, '//h2[text()="Булки"]') # Заголовок раздела "Булки"
    BUNS_BUTTON = (By.XPATH, '//span[text()="Булки"]')  # Кнопка "Булки"
    SAUCES_BUTTON = (By.XPATH, '//span[text()="Соусы"]')  # Кнопка "Соусы"
    FILLINGS_BUTTON = (By.XPATH, '//span[text()="Начинки"]')  # Кнопка "Начинки"
