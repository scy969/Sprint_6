from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTIONS = (By.CLASS_NAME, "accordion__button")
    ANSWERS = (By.CLASS_NAME, "accordion__panel")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FourPart__1uthg")
    FAQ_HEADER = (By.XPATH, "//div[contains(@class, 'Home_SubHeader') and text()='Вопросы о важном']")

    @staticmethod
    def get_question_by_index(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def get_answer_by_index(index):
        return (By.ID, f"accordion__panel-{index}")

    HEADER_ORDER_BUTTON = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")
    SCOOTER_LOGO = (By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI")
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[text()='Статус заказа']")
    ORDER_INPUT = (By.CSS_SELECTOR, ".Header_Input__xIoUq")
    GO_BUTTON = (By.CSS_SELECTOR, ".Header_Button__28dPO")