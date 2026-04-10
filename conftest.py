import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    from pages.order_page import OrderPage
    return OrderPage(driver)

