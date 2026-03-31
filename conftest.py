import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config import BASE_URL
from src.pages.main_page.main_page import MainPage
from src.pages.order_page.order_page import OrderPage


def pytest_addoption(parser):
    """Добавление кастомных опций командной строки"""
    parser.addoption("--browser", action="store", default="firefox",
                     help="Browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    """Фикстура для инициализации драйвера"""
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)
    else:  # firefox по умолчанию
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=firefox_options)

    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Закрываем cookie-согласие если оно есть
    try:
        cookie_consent = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
        close_button = (By.XPATH, "//button[contains(text(), 'да') or contains(text(), 'Да')]")

        if WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(cookie_consent)
        ):
            try:
                driver.find_element(*close_button).click()
            except:
                pass
    except:
        pass

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    """Фикстура для MainPage"""
    page = MainPage(driver)
    page.wait_for_faq_section()
    return page


@pytest.fixture(scope="function")
def order_page(driver):
    """Фикстура для OrderPage"""
    return OrderPage(driver)


@pytest.fixture(scope="function")
def pages(main_page, order_page):
    """Фикстура, объединяющая все страницы"""
    return {
        "main": main_page,
        "order": order_page
    }