from locators.order_page_locators import OrderFormLocators
from locators.main_page_locators import DropDownListLocators

# Данные для заказа самоката
order_test_data = [
    {
        "name": "Андрюха",
        "surname": "Золотухин",
        "address": "ул. Ленина, 4",
        "metro": "Чистые пруды",
        "phone": "+79996662233",
        "date": "22.02.2026",
        "rental_period_locator": OrderFormLocators.list_item_two_days,
        "color_locator": OrderFormLocators.checkbox_black,
        "comment": "Позвонить за час",        
    },
    {
        "name": "Пэпэ",
        "surname": "Шнейновна",
        "address": "пр. Мира, 33",
        "metro": "Тверская",
        "phone": "89278880102",
        "date": "27.02.2026",
        "rental_period_locator": OrderFormLocators.list_item_four_days,
        "color_locator": OrderFormLocators.checkbox_grey,
        "comment": "Доставить быстрее",
    }
]

# Данные для FAQ
faq_test_data = [
    {
        "question_locator": DropDownListLocators.accordion_heading_1,
        "answer_locator": DropDownListLocators.accordion_text_1,
        "expected_text": "400 рублей",
        "description": "Вопрос о цене",
        "test_id": "question_1_price" 
    },
    {
        "question_locator": DropDownListLocators.accordion_heading_2,
        "answer_locator": DropDownListLocators.accordion_text_2,
        "expected_text": "один заказ — один самокат",
        "description": "Вопрос о нескольких самокатах",
        "test_id": "question_2_multiple_scooters"  
    },
    {
        "question_locator": DropDownListLocators.accordion_heading_3,
        "answer_locator": DropDownListLocators.accordion_text_3,
        "expected_text": "8 мая",
        "description": "Вопрос о расчете времени аренды",
        "test_id": "question_3_rental_time"
    },
    {
        "question_locator": DropDownListLocators.accordion_heading_4,
        "answer_locator": DropDownListLocators.accordion_text_4,
        "expected_text": "завтрашнего дня",
        "description": "Вопрос о заказе на сегодня",
        "test_id": "question_4_today_order"
    },
    {
        "question_locator": DropDownListLocators.accordion_heading_5,
        "answer_locator": DropDownListLocators.accordion_text_5,
        "expected_text": "Пока что нет",
        "description": "Вопрос о продлении/возврате",
        "test_id": "question_5_extension"
    },
    {
        "question_locator": DropDownListLocators.accordion_heading_6,
        "answer_locator": DropDownListLocators.accordion_text_6,
        "expected_text": "полной зарядкой",
        "description": "Вопрос о зарядке",
        "test_id": "question_6_charging"
    },
    {
        "question_locator": DropDownListLocators.accordion_heading_7,
        "answer_locator": DropDownListLocators.accordion_text_7,
        "expected_text": "самокат не привезли",
        "description": "Вопрос об отмене заказа",
        "test_id": "question_7_cancellation"
    },
    {
        "question_locator": DropDownListLocators.accordion_heading_8,
        "answer_locator": DropDownListLocators.accordion_text_8,
        "expected_text": "обязательно",
        "description": "Вопрос о возврате самоката",
        "test_id": "question_8_return"
    }
]

faq_test_ids = [item["test_id"] for item in faq_test_data]
