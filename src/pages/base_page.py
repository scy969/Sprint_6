from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator, timeout=10):
        """Поиск элемента с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        """Поиск всех элементов по локатору"""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)

    def click_element(self, locator, timeout=10):
        """Клик по элементу с ожиданием и обработкой перекрытия"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except ElementClickInterceptedException:
            # Если элемент перекрыт, пробуем закрыть cookie-согласие
            self._close_cookie_consent()
            # Повторяем клик
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()

    def _close_cookie_consent(self):
        """Закрытие модального окна с cookie-согласием"""
        try:
            cookie_consent = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
            close_button = (By.XPATH,
                            "//button[contains(text(), 'да') or contains(text(), 'Да') or contains(text(), 'ок')]")

            if self.is_element_visible(cookie_consent, timeout=3):
                # Пробуем найти кнопку закрытия
                if self.is_element_visible(close_button, timeout=2):
                    self.click_element(close_button)
                else:
                    # Если нет кнопки, просто скроллим вниз
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except:
            pass

    def input_text(self, locator, text, timeout=10):
        """Ввод текста в поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        """Получение текста элемента"""
        element = self.find_element(locator, timeout)
        return element.text

    def get_attribute(self, locator, attribute, timeout=10):
        """Получение атрибута элемента"""
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)

    def is_element_visible(self, locator, timeout=10):
        """Проверка видимости элемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator, timeout=10):
        """Проверка наличия элемента в DOM"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, locator, timeout=10):
        """Проверка, что элемент кликабелен"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, locator, timeout=10):
        """Ожидание видимости элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_present(self, locator, timeout=10):
        """Ожидание наличия элемента в DOM"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        """Ожидание кликабельности элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def switch_to_new_window(self):
        """Переключение на новое окно"""
        current_handle = self.driver.current_window_handle
        self.wait.until(lambda d: len(d.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                break

    def switch_to_window_by_index(self, index):
        """Переключение на окно по индексу"""
        windows = self.driver.window_handles
        if index < len(windows):
            self.driver.switch_to.window(windows[index])

    def get_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url

    def get_current_window_handle(self):
        """Получение текущего окна"""
        return self.driver.current_window_handle

    def get_window_handles(self):
        """Получение всех окон"""
        return self.driver.window_handles

    def execute_script(self, script, *args):
        """Выполнение JavaScript"""
        return self.driver.execute_script(script, *args)

    def scroll_to_element(self, element):
        """Скролл до элемента"""
        self.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_element_by_locator(self, locator):
        """Скролл до элемента по локатору"""
        element = self.find_element(locator)
        self.scroll_to_element(element)

    def scroll_to_bottom(self):
        """Скролл вниз страницы"""
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """Скролл вверх страницы"""
        self.execute_script("window.scrollTo(0, 0);")

    def wait_for_url_change(self, expected_url_part, timeout=10):
        """Ожидание изменения URL"""
        self.wait.until(
            EC.url_contains(expected_url_part)
        )