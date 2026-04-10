import allure
import pytest
from data import order_test_data
from config import MAIN_PAGE
from locators.main_page_locators import OrderButtonsLocators


@allure.epic("Сервис аренды самокатов")
@allure.feature("Оформление заказа")            
class TestOrder:
    
    @allure.title("Тест заказа самоката")
    @allure.link("https://qa-scooter.praktikum-services.ru")
    @pytest.mark.parametrize("order_data, button_locator", [
        (order_test_data[0], OrderButtonsLocators.order_button),
        (order_test_data[1], OrderButtonsLocators.bottom_order_button),
    ], ids=[
        "top_button_with_andryha_data",
        "bottom_button_with_pepe_data"
    ])
    def test_successful_order(self, driver, main_page, order_page, order_data, button_locator):
        driver.get(MAIN_PAGE)
        main_page.close_cookie_banner()
        
        if button_locator == OrderButtonsLocators.order_button:
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()
        
        order_page.fill_first_form(order_data)
        order_page.click_next_button()
        order_page.fill_second_form(order_data)
        order_page.click_form_order_button()
        order_page.confirm_order()
        
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message