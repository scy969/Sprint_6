import allure
from pages.base_page import BasePage
from config import MAIN_PAGE
from locators.main_page_locators import (
    OrderButtonsLocators, 
    LogoLocators,
    CookieBannerLocator  
)

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        """Открыть главную страницу сервиса"""
        self.open_url(MAIN_PAGE)

    @allure.step("Открыть страницу заказа")
    def open_order_page(self):
        from config import ORDER_PAGE
        self.open_url(ORDER_PAGE)

    # кнопки заказать
    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(OrderButtonsLocators.order_button)
    
    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.click_element(OrderButtonsLocators.bottom_order_button)
    
    # раздел FAQ
    @allure.step("Кликнуть на вопрос FAQ")
    def click_faq_question(self, question_locator):
        self.click_element(question_locator)
    
    @allure.step("Получить текст ответа на вопрос FAQ")
    def get_faq_answer_text(self, answer_locator):
        self.wait_element_visible(answer_locator)
        return self.get_text(answer_locator)

    @allure.step("Безопасный клик по вопросу FAQ")
    def click_faq_question_safe(self, question_locator):
        """
        Безопасный клик по вопросу FAQ с прокруткой и ожиданием
        """
        self.safe_click_with_scroll(question_locator, offset=-300)
    
    # логотипы
    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(LogoLocators.logo_yandex)
    
    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(LogoLocators.logo_samokat)

    # баннер про куки
    @allure.step("Закрыть баннер с куками")
    def close_cookie_banner(self):
        self.wait_element_clickable(CookieBannerLocator.cookie_banner, timeout=3)
        self.click_element(CookieBannerLocator.cookie_banner)