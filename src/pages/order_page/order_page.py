from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.pages.base_page import BasePage
from src.pages.order_page.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_form(self, order_data):
        """
        Заполнение первой формы заказа
        :param order_data: dict с данными заказа
        """
        # Заполняем имя
        self.input_text(OrderPageLocators.NAME_INPUT, order_data["name"])

        # Заполняем фамилию
        self.input_text(OrderPageLocators.SURNAME_INPUT, order_data["surname"])

        # Заполняем адрес
        self.input_text(OrderPageLocators.ADDRESS_INPUT, order_data["address"])

        # Выбор станции метро
        self._select_metro(order_data["metro"])

        # Заполняем телефон
        self.input_text(OrderPageLocators.PHONE_INPUT, order_data["phone"])

    def _select_metro(self, metro_station):
        """
        Выбор станции метро из выпадающего списка
        :param metro_station: название станции метро
        """
        # Кликаем по полю ввода метро
        self.click_element(OrderPageLocators.METRO_INPUT)

        # Вводим название станции
        metro_input = self.find_element(OrderPageLocators.METRO_INPUT)
        metro_input.clear()
        metro_input.send_keys(metro_station)

        # Ожидаем появления выпадающего списка
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".select-search__option"))
        )

        # Выбираем подходящую станцию
        metro_option = (By.XPATH,
                        f"//div[contains(@class, 'select-search__option') and contains(text(), '{metro_station}')]")

        try:
            self.click_element(metro_option, timeout=3)
        except:
            # Если не нашли по тексту, выбираем первый вариант
            first_option = (By.CSS_SELECTOR, ".select-search__option")
            self.click_element(first_option)

    def click_next_button(self):
        """Клик по кнопке Далее"""
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        # Ожидаем загрузки второй формы
        self.wait_for_element_visible(OrderPageLocators.DATE_INPUT)

    def click_next_button_without_wait(self):
        """Клик по кнопке Далее без ожидания второй формы (для тестов валидации)"""
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, order_data):
        """
        Заполнение второй формы заказа
        :param order_data: dict с данными заказа
        """
        # Выбор даты
        self._select_date(order_data["date"])

        # Выбор срока аренды
        self._select_rental_period(order_data["rental_period"])

        # Выбор цвета самоката
        if order_data.get("color") == "black":
            self.click_element(OrderPageLocators.SCOOTER_COLOR_BLACK)
        elif order_data.get("color") == "grey":
            self.click_element(OrderPageLocators.SCOOTER_COLOR_GREY)

        # Комментарий для курьера
        if order_data.get("comment"):
            self.input_text(OrderPageLocators.COMMENT_INPUT, order_data["comment"])

    def _select_date(self, day):
        """
        Выбор даты в календаре
        :param day: число месяца
        """
        # Кликаем по полю ввода даты
        self.click_element(OrderPageLocators.DATE_INPUT)

        # Ожидаем появления календаря
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )

        # Выбираем нужную дату
        date_picker = OrderPageLocators.get_date_picker_day(str(day))
        self.click_element(date_picker)

    def _select_rental_period(self, period):
        """
        Выбор срока аренды
        :param period: срок аренды (сутки, двое суток, трое суток и т.д.)
        """
        # Кликаем по выпадающему списку
        self.click_element(OrderPageLocators.RENTAL_PERIOD)

        # Ожидаем появления опций
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".Dropdown-option"))
        )

        # Выбираем нужный период
        rental_option = OrderPageLocators.get_rental_period_option(period)
        self.click_element(rental_option)

    def submit_order(self):
        """Отправка заказа (клик по кнопке Заказать)"""
        self.click_element(OrderPageLocators.FINAL_ORDER_BUTTON)

    def confirm_order(self):
        """Подтверждение заказа в модальном окне"""
        # Ожидаем появления модального окна
        self.wait_for_element_visible(OrderPageLocators.CONFIRM_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    def is_order_successful(self, timeout=10):
        """Проверка успешного создания заказа"""
        try:
            self.wait_for_element_visible(OrderPageLocators.SUCCESS_MESSAGE, timeout)
            return True
        except TimeoutException:
            return False

    def get_success_message_text(self):
        """Получение текста сообщения об успехе"""
        try:
            message = self.wait_for_element_visible(OrderPageLocators.SUCCESS_MESSAGE)
            return message.text
        except:
            return ""

    def complete_order_flow(self, order_data):
        """
        Полный флоу оформления заказа
        :param order_data: dict с данными заказа
        """
        self.fill_first_form(order_data)
        self.click_next_button()
        self.fill_second_form(order_data)
        self.submit_order()
        self.confirm_order()

    def wait_for_first_form(self, timeout=10):
        """Ожидание загрузки первой формы заказа"""
        self.wait_for_element_visible(OrderPageLocators.NAME_INPUT, timeout)

    def is_first_form_visible(self, timeout=5):
        """Проверка видимости первой формы заказа"""
        try:
            self.wait_for_element_visible(OrderPageLocators.NAME_INPUT, timeout)
            return True
        except TimeoutException:
            return False

    def wait_for_second_form(self, timeout=10):
        """Ожидание загрузки второй формы заказа"""
        self.wait_for_element_visible(OrderPageLocators.DATE_INPUT, timeout)

    def is_second_form_visible(self, timeout=5):
        """Проверка видимости второй формы заказа"""
        try:
            self.wait_for_element_visible(OrderPageLocators.DATE_INPUT, timeout)
            return True
        except TimeoutException:
            return False

    def wait_for_success_message(self, timeout=10):
        """Ожидание появления сообщения об успехе"""
        self.wait_for_element_visible(OrderPageLocators.SUCCESS_MESSAGE, timeout)

    def get_current_step_header(self):
        """Получение заголовка текущего шага формы"""
        header = (By.CLASS_NAME, "Order_Header__BZXOb")
        return self.get_text(header)