from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import data


class TestStellarBurgers:
    def test_fillings(self, driver):
    # Открываем главную страницу
        driver.get(data.MAIN_PAGE)
    # проверяем наличие на странице раздела конструктора
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_CONTAINER))
    # Нажимаем на кнопку "Начинки"
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
    # ждем появления на странице ингредиента "Мясо бессмертных моллюсков Protostomia"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (Locators.MEAT_FILLING))
        )
        assert 'tab_tab_type_current' in driver.find_element(*Locators.FILLINGS_BUTTON).get_attribute('class')


    def test_sauces(self, driver):
    # Открываем главную страницу
        driver.get(data.MAIN_PAGE)
    # проверяем наличие на странице раздела конструктора
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_CONTAINER))

    # Нажимаем на кнопку "Начинки"
        driver.find_element(*Locators.FILLINGS_BUTTON).click()

    # ждем появления на странице ингредиента "Мясо бессмертных моллюсков Protostomia"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (Locators.MEAT_FILLING))
        )

    # Нажимаем на кнопку "Соусы" (переходим к тестируемому разделу)
        driver.find_element(*Locators.SAUCES_BUTTON).click()

    # ждем появления на странице ингредиента "Соус Spicy-X"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (Locators.SPICY_SAUCE))
        )
        assert 'tab_tab_type_current' in driver.find_element(*Locators.SAUCES_BUTTON).get_attribute('class')

    def test_buns(self, driver):
    # Открываем главную страницу
        driver.get(data.MAIN_PAGE)
    # проверяем наличие на странице раздела конструктора
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_CONTAINER))

    # Нажимаем на кнопку "Начинки"
        driver.find_element(*Locators.FILLINGS_BUTTON).click()

    # ждем появления на странице ингредиента "Мясо бессмертных моллюсков Protostomia"
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (Locators.HEADER_FILLINGS))
        )

    # Нажимаем на кнопку "Булки" (переходим к тестируемому разделу)
        driver.find_element(*Locators.BUNS_BUTTON).click()

    # ждем появления на странице ингредиента "Флюоресцентная булка R2-D3"
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (Locators.FLUOR_BUN))
        )
        assert 'tab_tab_type_current' in driver.find_element(*Locators.BUNS_BUTTON).get_attribute('class')













