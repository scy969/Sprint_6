import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу: {url}")
    def open_url(self, url):
        """Открыть указанный URL в браузере"""
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Ввести текст: {text}")
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def wait_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидать и кликнуть по динамическому элементу")
    def wait_and_click_dynamic(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Прокрутить страницу до элемента по локатору")
    def scroll_to_element_by_locator(self, locator):
        element = self.find_element(locator)
        self.scroll_to_element(element)

    @allure.step("Прокрутить до элемента со смещением вверх")
    def scroll_to_element_with_offset(self, locator, offset=-300):
        """
        Прокручивает страницу так, чтобы элемент оказался в центре,
        затем смещает вверх на указанное количество пикселей
        """
        element = self.find_element(locator)
        self.driver.execute_script(
            f"arguments[0].scrollIntoView({{block: 'center', behavior: 'instant'}}); "
            f"window.scrollBy(0, {offset});",
            element
        )

    @allure.step("Безопасный клик по элементу с предварительной прокруткой")
    def safe_click_with_scroll(self, locator, offset=-300):
        """
        Прокручивает к элементу со смещением, ожидает кликабельности и кликает
        """
        self.scroll_to_element_with_offset(locator, offset)
        self.wait_element_clickable(locator)
        self.click_element(locator)

    @allure.step("Получить текущее окно")
    def get_current_window(self):
        return self.driver.current_window_handle

    @allure.step("Переключиться на последнее открытое окно")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидать URL: {expected_url}")
    def wait_for_url_to_be(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(expected_url)
        )

    @allure.step("Ожидать открытия нового окна")
    def wait_for_new_window(self, count=2, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(count)
        )