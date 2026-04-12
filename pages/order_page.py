import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderFormLocators


class OrderPage(BasePage):

    @allure.step("Заполнить первую часть формы")
    def fill_first_form(self, data):
        self.send_keys(OrderFormLocators.name_input_field, data["name"])
        self.send_keys(OrderFormLocators.surname_input_field, data["surname"])
        self.send_keys(OrderFormLocators.address_input_field, data["address"])
        self.click_element(OrderFormLocators.metro_input_field)

        metro_station_locator = OrderFormLocators.get_metro_station_locator(data['metro'])
        self.wait_and_click_dynamic(metro_station_locator)

        self.send_keys(OrderFormLocators.telephone_input_field, data["phone"])

    @allure.step("Заполнить вторую часть формы")
    def fill_second_form(self, data):
        # Заполнение даты
        self.send_keys(OrderFormLocators.date_input_field, data["date"])

        # Закрыть календарь - клик по заголовку формы
        self.click_element(OrderFormLocators.form_title)

        # Выбор срока аренды
        self.click_element(OrderFormLocators.rental_period_list)
        self.wait_and_click_dynamic(data["rental_period_locator"])  # ← ключ из данных

        # Выбор цвета самоката
        self.click_element(data["color_locator"])  # ← ключ из данных

        # Комментарий для курьера
        if data.get("comment"):
            self.send_keys(OrderFormLocators.comment_input_field, data["comment"])

    @allure.step("Закрыть календарь")
    def close_calendar(self):
        """Закрыть календарь, кликнув по заголовку формы"""
        self.click_element(OrderFormLocators.form_title)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_element(OrderFormLocators.next_button)

    @allure.step("Нажать кнопку 'Заказать' в форме")
    def click_form_order_button(self):
        self.click_element(OrderFormLocators.form_order_button)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.wait_element_clickable(OrderFormLocators.order_confirm_button)
        self.click_element(OrderFormLocators.order_confirm_button)

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        self.wait_element_visible(OrderFormLocators.modal_window)
        return self.get_text(OrderFormLocators.modal_window)