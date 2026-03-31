from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from src.pages.main_page.main_page_locators import MainPageLocators
from src.pages.base_page import BasePage
import time


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_questions(self):
        """Получить все вопросы"""
        return self.driver.find_elements(*MainPageLocators.QUESTIONS)

    def get_answers(self):
        """Получить все ответы"""
        return self.driver.find_elements(*MainPageLocators.ANSWERS)

    def get_question_by_index(self, index):
        """Получить вопрос по индексу"""
        return self.driver.find_element(*MainPageLocators.get_question_by_index(index))

    def get_answer_by_index(self, index):
        """Получить ответ по индексу"""
        return self.driver.find_element(*MainPageLocators.get_answer_by_index(index))

    def scroll_to_element(self, element):
        """
        Прокрутка к элементу с отступом сверху
        Имитирует поведение пользователя, который скроллит до нужного элемента
        """
        self.driver.execute_script("""
            arguments[0].scrollIntoView({block: 'start', behavior: 'smooth'});
            window.scrollBy(0, -100);
        """, element)
        time.sleep(0.5)

    def click_question_by_index(self, index):
        """
        Клик по вопросу по индексу с гарантированной видимостью
        """
        element = self.get_question_by_index(index)
        self.scroll_to_element(element)

        is_visible = self.driver.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return rect.top >= 0 && rect.bottom <= window.innerHeight;
        """, element)

        if not is_visible:
            self.scroll_to_element(element)

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                self.wait.until(
                    EC.element_to_be_clickable(element)
                ).click()
                return
            except ElementClickInterceptedException:
                if attempt == max_attempts - 1:
                    raise
                time.sleep(0.5)

    def is_answer_visible_by_index(self, index):
        """Проверка видимости ответа по индексу"""
        try:
            answer = self.get_answer_by_index(index)
            return answer.is_displayed()
        except:
            return False

    def get_answer_text_by_index(self, index):
        """Получение текста ответа по индексу"""
        try:
            answer = self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.get_answer_by_index(index))
            )
            return answer.text
        except TimeoutException:
            return ""

    def is_faq_section_visible(self):
        """Проверить видимость раздела FAQ"""
        try:
            section = self.driver.find_element(*MainPageLocators.FAQ_SECTION)
            return section.is_displayed()
        except:
            return False

    def get_faq_header_text(self):
        """Получить текст заголовка раздела FAQ"""
        header = self.driver.find_element(*MainPageLocators.FAQ_HEADER)
        return header.text

    def wait_for_faq_section(self):
        """Ожидание загрузки раздела FAQ"""
        self.wait.until(
            EC.presence_of_element_located(MainPageLocators.FAQ_SECTION)
        )

    # ========== НОВЫЕ МЕТОДЫ ДЛЯ РАБОТЫ С ЗАКАЗАМИ ==========

    def open(self):
        """Открытие главной страницы"""
        # Используем BASE_URL из config, если нужно
        # self.driver.get(BASE_URL)
        # Или просто обновляем страницу, если она уже открыта
        pass  # Убираем, так как driver уже открывает страницу в conftest

    def click_header_order_button(self):
        """Клик по кнопке заказа в шапке"""
        self.click_element(MainPageLocators.HEADER_ORDER_BUTTON)

    def click_bottom_order_button(self):
        """Клик по кнопке заказа внизу страницы"""
        self.scroll_to_element_by_locator(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def is_header_order_button_visible(self):
        """Проверка видимости кнопки заказа в шапке"""
        return self.is_element_visible(MainPageLocators.HEADER_ORDER_BUTTON)

    def is_bottom_order_button_visible(self):
        """Проверка видимости кнопки заказа внизу"""
        self.scroll_to_element_by_locator(MainPageLocators.BOTTOM_ORDER_BUTTON)
        return self.is_element_visible(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def scroll_to_element_by_locator(self, locator):
        """Скролл до элемента по локатору"""
        element = self.find_element(locator)
        self.scroll_to_element(element)

    def get_header_order_button_text(self):
        """Получить текст кнопки заказа в шапке"""
        return self.get_text(MainPageLocators.HEADER_ORDER_BUTTON)

    def get_bottom_order_button_text(self):
        """Получить текст кнопки заказа внизу"""
        return self.get_text(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def wait_for_page_load(self):
        """Ожидание загрузки главной страницы"""
        self.wait.until(
            EC.presence_of_element_located(MainPageLocators.HEADER_ORDER_BUTTON)
        )

    def is_logo_visible(self):
        """Проверка видимости логотипа Самоката"""
        return self.is_element_visible(MainPageLocators.SCOOTER_LOGO)

    def is_yandex_logo_visible(self):
        """Проверка видимости логотипа Яндекса"""
        return self.is_element_visible(MainPageLocators.YANDEX_LOGO)

    # ========== ДОПОЛНИТЕЛЬНЫЕ МЕТОДЫ ДЛЯ УДОБСТВА ==========

    def click_order_button_and_wait(self, button_type="header"):
        """
        Клик по кнопке заказа и ожидание перехода на страницу заказа
        :param button_type: "header" или "bottom"
        """
        if button_type == "header":
            self.click_header_order_button()
        else:
            self.click_bottom_order_button()

        # Ожидаем появления элемента формы заказа
        from src.pages.order_page.order_page_locators import OrderPageLocators
        self.wait.until(
            EC.presence_of_element_located(OrderPageLocators.NAME_INPUT)
        )
        time.sleep(0.5)

    def get_all_order_buttons(self):
        """
        Получить все кнопки заказа на странице
        Возвращает список веб-элементов
        """
        header_button = self.driver.find_element(*MainPageLocators.HEADER_ORDER_BUTTON)
        bottom_button = self.driver.find_element(*MainPageLocators.BOTTOM_ORDER_BUTTON)
        return [header_button, bottom_button]

    def is_order_button_enabled(self, button_type="header"):
        """
        Проверка, активна ли кнопка заказа
        :param button_type: "header" или "bottom"
        """
        if button_type == "header":
            button = self.find_element(MainPageLocators.HEADER_ORDER_BUTTON)
        else:
            button = self.find_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        return button.is_enabled()

    def wait_for_header_order_button(self):
        """Ожидание появления кнопки заказа в шапке"""
        self.wait.until(
            EC.presence_of_element_located(MainPageLocators.HEADER_ORDER_BUTTON)
        )

    def wait_for_bottom_order_button(self):
        """Ожидание появления кнопки заказа внизу"""
        self.wait.until(
            EC.presence_of_element_located(MainPageLocators.BOTTOM_ORDER_BUTTON)
        )

    def get_header_order_button_attribute(self, attribute):
        """Получить атрибут кнопки заказа в шапке"""
        return self.get_attribute(MainPageLocators.HEADER_ORDER_BUTTON, attribute)

    def get_bottom_order_button_attribute(self, attribute):
        """Получить атрибут кнопки заказа внизу"""
        return self.get_attribute(MainPageLocators.BOTTOM_ORDER_BUTTON, attribute)

    def is_header_button_clickable(self):
        """Проверка, кликабельна ли кнопка в шапке"""
        return self.is_element_clickable(MainPageLocators.HEADER_ORDER_BUTTON)

    def is_bottom_button_clickable(self):
        """Проверка, кликабельна ли кнопка внизу"""
        self.scroll_to_element_by_locator(MainPageLocators.BOTTOM_ORDER_BUTTON)
        return self.is_element_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def get_current_url(self):
        """Получить текущий URL страницы"""
        return self.driver.current_url

    def refresh_page(self):
        """Обновить страницу"""
        self.driver.refresh()
        time.sleep(1)

    def scroll_to_bottom(self):
        """Скролл вниз страницы"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)

    def scroll_to_top(self):
        """Скролл вверх страницы"""
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)

    def wait_for_url_change(self, expected_url_part, timeout=10):
        """
        Ожидание изменения URL
        :param expected_url_part: ожидаемая часть URL
        """
        self.wait.until(
            EC.url_contains(expected_url_part)
        )

    def get_window_handles(self):
        """Получить все открытые окна"""
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        """Переключиться на конкретное окно"""
        self.driver.switch_to.window(window_handle)

    def _close_cookie_consent(self):
        """Закрытие модального окна с cookie-согласием"""
        try:
            cookie_consent = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
            close_button = (By.XPATH, "//button[contains(text(), 'да') or contains(text(), 'Да')]")

            if self.is_element_visible(cookie_consent, timeout=3):
                if self.is_element_visible(close_button, timeout=2):
                    self.click_element(close_button)
        except:
            pass

    def click_bottom_order_button(self):
        """Клик по кнопке заказа внизу страницы"""
        # Сначала закрываем cookie если нужно
        self._close_cookie_consent()
        # Скроллим до кнопки
        self.scroll_to_element_by_locator(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)