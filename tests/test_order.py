import allure
from data import order_test_data


@allure.epic("Сервис аренды самокатов")
@allure.feature("Оформление заказа")
class TestOrder:

    @allure.title("Тест заказа самоката через верхнюю кнопку")
    @allure.link("https://qa-scooter.praktikum-services.ru")
    def test_successful_order_top_button(self, driver, main_page, order_page):
        main_page.open_main_page()  # ← Исправлено
        main_page.close_cookie_banner()
        main_page.click_top_order_button()

        order_page.fill_first_form(order_test_data[0])
        order_page.click_next_button()
        order_page.fill_second_form(order_test_data[0])
        order_page.click_form_order_button()
        order_page.confirm_order()

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message

    @allure.title("Тест заказа самоката через нижнюю кнопку")
    @allure.link("https://qa-scooter.praktikum-services.ru")
    def test_successful_order_bottom_button(self, driver, main_page, order_page):
        main_page.open_main_page()  # ← исправлено: вместо driver.get(MAIN_PAGE)
        main_page.close_cookie_banner()
        main_page.click_bottom_order_button()

        order_page.fill_first_form(order_test_data[1])
        order_page.click_next_button()
        order_page.fill_second_form(order_test_data[1])
        order_page.click_form_order_button()
        order_page.confirm_order()

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message