from selenium.webdriver.common.by import By


class OrderFormLocators:
    # локаторы формы заказа
    # названия формы "Для кого самокат"
    form_title = [By.CLASS_NAME, "Order_Header__BZXOb"]
    # поле ввода имени
    name_input_field = [By.XPATH, "//input[@type='text' and contains(@placeholder, 'Имя')]"]
    # поле ввода фамилии
    surname_input_field = [By.XPATH, "//input[@type='text' and contains(@placeholder, 'Фамилия')]"]
    # поле ввода адреса
    address_input_field = [By.XPATH, "//input[@type='text' and contains(@placeholder, 'Адрес')]"]
    # выбор станции метро
    metro_input_field = [By.CLASS_NAME, "select-search__value"]
    # поле ввода телефона
    telephone_input_field = [By.XPATH, "//input[@type='text' and contains(@placeholder, 'Телефон')]"]
    # кнопка Далее
    next_button = [By.XPATH, "//button[text()='Далее']"]

    # НОВЫЙ ЛОКАТОР: динамический выбор станции метро
    @staticmethod
    def get_metro_station_locator(station_name):
        """Возвращает локатор для конкретной станции метро по названию"""
        return [By.XPATH, f"//div[text()='{station_name}']"]

    # поле выбора даты заказа
    date_input_field = [By.XPATH, "//input[@type='text' and contains(@placeholder, 'Когда привезти самокат')]"]
    # выпадающий список выбора срока аренды
    rental_period_list = [By.CLASS_NAME, "Dropdown-root"]

    # НОВЫЕ ЛОКАТОРЫ: элементы выпадающего списка срока аренды (динамические)
    @staticmethod
    def get_rental_period_locator(period_text):
        """Возвращает локатор для срока аренды по тексту"""
        return [By.XPATH, f"//div[@class='Dropdown-option' and text() = '{period_text}']"]

    # элементы выпадающего списка с выбором срока (конкретные значения)
    list_item_two_days = [By.XPATH, "//div[@class='Dropdown-option' and text() = 'двое суток']"]
    list_item_four_days = [By.XPATH, "//div[@class='Dropdown-option' and text() = 'четверо суток']"]

    # чекбокс выбора цвета
    checkbox_black = [By.ID, "black"]
    checkbox_grey = [By.ID, "grey"]

    # НОВЫЙ ЛОКАТОР: динамический выбор цвета
    @staticmethod
    def get_color_checkbox_locator(color_id):
        """Возвращает локатор для чекбокса цвета по ID"""
        return [By.ID, color_id]

    # поле ввода комментария
    comment_input_field = [By.XPATH, "//input[@type='text' and contains(@placeholder, 'Комментарий для курьера')]"]
    # кнопка заказать в форме заказа
    form_order_button = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    # кнопка подтверждения заказа Да
    order_confirm_button = [By.XPATH, "//button[text()='Да']"]
    # модальное окно с текстом Заказ оформлен
    modal_window = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']"]