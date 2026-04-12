from selenium.webdriver.common.by import By

class CookieBannerLocator:
    cookie_banner = [By.CLASS_NAME, 'App_CookieButton__3cvqF']

class LogoLocators:
    #локаторы логотипов
    logo_yandex = [By.XPATH, "//img[@alt = 'Yandex']"]
    logo_samokat = [By.XPATH, "//img[@alt = 'Scooter']"]

class OrderButtonsLocators:
    # локатор кнопки "Заказать" в шапке страницы
    order_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    #локатор кнопки "Заказать" внизу страницы
    bottom_order_button = [By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM']


class DropDownListLocators:
    # локаторы элементов выпадающего списка с первого по восьмой
    accordion_heading_1 = [By.ID, 'accordion__heading-0']
    accordion_heading_2 = [By.ID, 'accordion__heading-1']
    accordion_heading_3 = [By.ID, 'accordion__heading-2']
    accordion_heading_4 = [By.ID, 'accordion__heading-3']
    accordion_heading_5 = [By.ID, 'accordion__heading-4']
    accordion_heading_6 = [By.ID, 'accordion__heading-5']
    accordion_heading_7 = [By.ID, 'accordion__heading-6']
    accordion_heading_8 = [By.ID, 'accordion__heading-7']
    # локаторы выпадающих ответов
    accordion_text_1 = [By.XPATH, "//p[contains(text(), 'Сутки — 400 рублей')]"]
    accordion_text_2 = [By.XPATH, "//p[contains(text(), 'Пока что у нас так: один заказ — один самокат')]"]
    accordion_text_3 = [By.XPATH, "//p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая')]"]
    accordion_text_4 = [By.XPATH, "//p[contains(text(), 'Только начиная с завтрашнего дня')]"]
    accordion_text_5 = [By.XPATH, "//p[contains(text(), 'Пока что нет! Но если что-то срочное')]"]
    accordion_text_6 = [By.XPATH, "//p[contains(text(), 'Самокат приезжает к вам с полной зарядкой')]"]
    accordion_text_7 = [By.XPATH, "//p[contains(text(), 'Да, пока самокат не привезли')]"]
    accordion_text_8 = [By.XPATH, "//p[contains(text(), 'Да, обязательно. Всем самокатов!')]"]
