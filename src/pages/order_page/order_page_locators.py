from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поля первой формы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CSS_SELECTOR, ".select-search__input")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка "Далее"
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Поля второй формы
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    SCOOTER_COLOR_BLACK = (By.XPATH, "//label[text()='чёрный жемчуг']/input")
    SCOOTER_COLOR_GREY = (By.XPATH, "//label[text()='серая безысходность']/input")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопки финального оформления
    FINAL_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Сообщение об успешном создании заказа
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZlBH")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    # Статический метод для выбора даты в календаре
    @staticmethod
    def get_date_picker_day(day):
        return (By.XPATH,
                f"//div[contains(@class, 'react-datepicker__day') and text()='{day}' and not(contains(@class, 'react-datepicker__day--outside-month'))]")

    # Статический метод для выбора срока аренды
    @staticmethod
    def get_rental_period_option(period):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")