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
    # поле выбора даты заказа
    date_input_field = [By.XPATH, "//input[@type='text' and contains(@placeholder, 'Когда привезти самокат')]"]
    # выпадающий список выбора срока аренды
    rental_period_list = [By.CLASS_NAME, "Dropdown-root"]
    # элемент выпадающего списка с выбором срока двое суток
    list_item_two_days = [By.XPATH, "//div[@class='Dropdown-option' and text() = 'двое суток']"]
    # элемент выпадающего списка с выбором срока четверо суток
    list_item_four_days = [By.XPATH, "//div[@class='Dropdown-option' and text() = 'четверо суток']"]
    # чекбокс выбора черно цвета
    checkbox_black = [By.ID, "black"]
    # чекбокс выбора серого цвета
    checkbox_grey = [By.ID, "grey"]
    # поле ввода комментария 
    comment_input_field = [By.XPATH, "//input[@type='text' and contains(@placeholder, 'Комментарий для курьера')]"]
    # кнопка заказать в форме заказа
    form_order_button = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    # кнопка подтверждения заказа Да
    order_confirm_button = [By.XPATH, "//button[text()='Да']"]
    # модальное окно с текстом Заказ оформлен
    modal_window = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']"]
