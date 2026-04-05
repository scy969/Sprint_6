from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from src.pages.main_page.main_page_locators import MainPageLocators
from src.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_questions(self):
        return self.find_elements(MainPageLocators.QUESTIONS)

    def get_answers(self):
        return self.find_elements(MainPageLocators.ANSWERS)

    def get_question_by_index(self, index):
        return self.find_element(MainPageLocators.get_question_by_index(index))

    def get_answer_by_index(self, index):
        return self.find_element(MainPageLocators.get_answer_by_index(index))

    def scroll_to_element(self, element):
        self.execute_script("""
            arguments[0].scrollIntoView({block: 'start', behavior: 'smooth'});
            window.scrollBy(0, -100);
        """, element)
        self.wait_for_element_clickable(MainPageLocators.QUESTIONS)

    def click_question_by_index(self, index):
        element = self.get_question_by_index(index)

        # Скроллим пока элемент не окажется в центре видимой области
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        # Небольшая пауза после скролла
        import time
        time.sleep(0.5)

        # Пробуем кликнуть обычным способом
        try:
            element.click()
        except ElementClickInterceptedException:
            # Если не получилось - скроллим еще выше и повторяем
            self.driver.execute_script("window.scrollBy(0, -100);")
            time.sleep(0.5)
            element.click()

    def is_answer_visible_by_index(self, index):
        return self.is_element_visible(MainPageLocators.get_answer_by_index(index))

    def get_answer_text_by_index(self, index):
        try:
            answer = self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.get_answer_by_index(index))
            )
            return answer.text
        except TimeoutException:
            return ""

    def is_faq_section_visible(self):
        return self.is_element_visible(MainPageLocators.FAQ_SECTION)

    def get_faq_header_text(self):
        return self.get_text(MainPageLocators.FAQ_HEADER)

    def wait_for_faq_section(self):
        self.wait.until(
            EC.presence_of_element_located(MainPageLocators.FAQ_SECTION)
        )

    def open(self):
        pass

    def click_header_order_button(self):
        self.click_element(MainPageLocators.HEADER_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self._close_cookie_consent()
        self.scroll_to_element_by_locator(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def is_header_order_button_visible(self):
        return self.is_element_visible(MainPageLocators.HEADER_ORDER_BUTTON)

    def is_bottom_order_button_visible(self):
        self.scroll_to_element_by_locator(MainPageLocators.BOTTOM_ORDER_BUTTON)
        return self.is_element_visible(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def scroll_to_element_by_locator(self, locator):
        element = self.find_element(locator)
        self.scroll_to_element(element)

    def get_header_order_button_text(self):
        return self.get_text(MainPageLocators.HEADER_ORDER_BUTTON)

    def get_bottom_order_button_text(self):
        return self.get_text(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def wait_for_page_load(self):
        self.wait.until(
            EC.presence_of_element_located(MainPageLocators.HEADER_ORDER_BUTTON)
        )

    def is_logo_visible(self):
        return self.is_element_visible(MainPageLocators.SCOOTER_LOGO)

    def is_yandex_logo_visible(self):
        return self.is_element_visible(MainPageLocators.YANDEX_LOGO)

    def click_header_order_button_and_wait(self):
        self.click_header_order_button()
        from src.pages.order_page.order_page_locators import OrderPageLocators
        self.wait.until(
            EC.presence_of_element_located(OrderPageLocators.NAME_INPUT)
        )

    def click_bottom_order_button_and_wait(self):
        self.click_bottom_order_button()
        from src.pages.order_page.order_page_locators import OrderPageLocators
        self.wait.until(
            EC.presence_of_element_located(OrderPageLocators.NAME_INPUT)
        )

    def get_all_order_buttons(self):
        header_button = self.find_element(MainPageLocators.HEADER_ORDER_BUTTON)
        bottom_button = self.find_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        return [header_button, bottom_button]

    def is_header_order_button_enabled(self):
        button = self.find_element(MainPageLocators.HEADER_ORDER_BUTTON)
        return button.is_enabled()

    def is_bottom_order_button_enabled(self):
        button = self.find_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        return button.is_enabled()

    def wait_for_header_order_button(self):
        self.wait.until(
            EC.presence_of_element_located(MainPageLocators.HEADER_ORDER_BUTTON)
        )

    def wait_for_bottom_order_button(self):
        self.wait.until(
            EC.presence_of_element_located(MainPageLocators.BOTTOM_ORDER_BUTTON)
        )

    def get_header_order_button_attribute(self, attribute):
        return self.get_attribute(MainPageLocators.HEADER_ORDER_BUTTON, attribute)

    def get_bottom_order_button_attribute(self, attribute):
        return self.get_attribute(MainPageLocators.BOTTOM_ORDER_BUTTON, attribute)

    def is_header_button_clickable(self):
        return self.is_element_clickable(MainPageLocators.HEADER_ORDER_BUTTON)

    def is_bottom_button_clickable(self):
        self.scroll_to_element_by_locator(MainPageLocators.BOTTOM_ORDER_BUTTON)
        return self.is_element_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def get_current_url(self):
        return BasePage.get_current_url(self)

    def refresh_page(self):
        self.driver.refresh()
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

    def scroll_to_bottom(self):
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

    def scroll_to_top(self):
        self.execute_script("window.scrollTo(0, 0);")
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

    def wait_for_url_change(self, expected_url_part, timeout=10):
        self.wait.until(
            EC.url_contains(expected_url_part)
        )

    def get_window_handles(self):
        return BasePage.get_window_handles(self)

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
