class OrderData:
    """Тестовые данные для заказов"""

    # Первый набор данных
    FIRST_ORDER = {
        "name": "Иван",
        "surname": "Петров",
        "address": "ул. Ленина, д. 10, кв. 5",
        "metro": "Сокольники",
        "phone": "+79001234567",
        "date": "15",
        "rental_period": "сутки",
        "color": "black",
        "comment": "Позвоните за 10 минут до приезда"
    }

    # Второй набор данных
    SECOND_ORDER = {
        "name": "Анна",
        "surname": "Смирнова",
        "address": "пр. Мира, д. 25, стр. 1",
        "metro": "Комсомольская",
        "phone": "+79109876543",
        "date": "20",
        "rental_period": "двое суток",
        "color": "grey",
        "comment": "Домофон 123, код подъезда 456"
    }

    # Набор для негативного тестирования
    INVALID_ORDER = {
        "name": "",
        "surname": "",
        "address": "",
        "metro": "",
        "phone": "123",
        "date": "",
        "rental_period": "",
        "color": "",
        "comment": ""
    }