from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import time

class TestStellarBurgers:
    def test_constructor(self, driver):
    # Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")
    # проверяем наличие на странице раздела конструктора
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_CONTAINER))

    # Делаем скролл до раздела "Соусы"
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        sauces_header = driver.find_element(*Locators.HEADER_SAUCES)
        driver.execute_script("arguments[0].scrollIntoView();", sauces_header)
        assert sauces_header.is_displayed()
        time.sleep(2)# пауза для визуальной проверки отображения раздела

    # Делаем скролл до раздела "Начинки"
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        fillings_header = driver.find_element(*Locators.HEADER_FILLINGS)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_header)
        assert fillings_header.is_displayed()
        time.sleep(2) # пауза для визуальной проверки отображения раздела

    # Делаем скролл до раздела "Булки"
        driver.find_element(*Locators.BUNS_BUTTON).click()
        buns_header = driver.find_element(*Locators.HEADER_BUNS)
        driver.execute_script("arguments[0].scrollIntoView();", buns_header)
        assert buns_header.is_displayed()
        time.sleep(2) # пауза для визуальной проверки отображения раздела










