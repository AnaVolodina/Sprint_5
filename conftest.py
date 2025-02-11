import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome() # запускаем браузер
    driver.implicitly_wait(10) # неявное ожидание
    yield driver  # Передаем экземпляр драйвера тестам
    driver.quit()  # Закрываем браузер после завершения всех тестов