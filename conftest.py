import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)

