import allure
from config import MAIN_PAGE, DZEN_PAGE

@allure.epic("Сервис аренды самокатов")
@allure.feature("Навигация по логотипам")
class TestNavigation:

    @allure.story("Логотип Самоката")
    @allure.title("Тест навигации: логотип Самоката ведет на главную страницу")
    def test_scooter_logo_navigation(self, driver, main_page):
        main_page.open_order_page()
        main_page.click_scooter_logo()
        main_page.wait_for_url_to_be(MAIN_PAGE)

        with allure.step("Проверить, что URL соответствует главной странице"):
            assert main_page.get_current_url() == MAIN_PAGE

    @allure.story("Логотип Яндекса")
    @allure.title("Тест навигации: логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_navigation(self, driver, main_page):
        main_page.open_main_page()
        main_page.click_yandex_logo()
        main_page.wait_for_new_window()
        main_page.switch_to_new_window()
        main_page.wait_for_url_to_be(DZEN_PAGE)

        with allure.step("Проверить, что открылся Дзен"):
            assert main_page.get_current_url() == DZEN_PAGE