import allure
from pages.base_page import BasePage
from locators.main_page_locators import (
    OrderButtonsLocators, 
    LogoLocators,
    CookieBannerLocator  
)

class MainPage(BasePage):

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
        element = self.find_element(question_locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'}); "
            "window.scrollBy(0, -300);",  # Смещаем вверх на 100px
            element
        )
        self.wait_element_clickable(question_locator)
        self.click_element(question_locator)
    
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