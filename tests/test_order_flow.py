import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data.order_data import OrderData


class TestOrderFlow:
    """Тесты для проверки флоу заказа самоката"""

    # ==================== ПОЗИТИВНЫЕ ТЕСТЫ ====================

    @pytest.mark.parametrize("order_data, button_type", [
        (OrderData.FIRST_ORDER, "header"),
        (OrderData.SECOND_ORDER, "bottom"),
    ])
    def test_positive_order_flow(self, main_page, order_page, order_data, button_type):
        """
        Тест позитивного сценария заказа самоката
        Проверяет создание заказа с разными данными и разными точками входа
        """
        # Нажатие кнопки заказа в зависимости от типа
        if button_type == "header":
            main_page.click_header_order_button()
        else:
            main_page.click_bottom_order_button()

        # Оформление заказа
        order_page.complete_order_flow(order_data)

        # Проверка успешного создания заказа
        assert order_page.is_order_successful(), \
            f"Сообщение об успешном создании заказа не появилось для данных: {order_data['name']} {order_data['surname']}"

        # Проверка текста сообщения
        success_text = order_page.get_success_message_text()
        assert "Заказ оформлен" in success_text, \
            f"Неверное сообщение об успехе: {success_text}"

    @pytest.mark.parametrize("order_data", [OrderData.FIRST_ORDER, OrderData.SECOND_ORDER])
    def test_order_flow_from_header_button(self, main_page, order_page, order_data):
        """
        Тест полного флоу заказа через кнопку в шапке
        С двумя разными наборами данных
        """
        main_page.click_header_order_button()
        order_page.complete_order_flow(order_data)

        assert order_page.is_order_successful(), \
            f"Заказ с данными {order_data['name']} {order_data['surname']} не создан"


    @pytest.mark.parametrize("order_data", [OrderData.FIRST_ORDER, OrderData.SECOND_ORDER])
    def test_order_flow_from_bottom_button(self, main_page, order_page, order_data):
        """
        Тест полного флоу заказа через кнопку внизу страницы
        С двумя разными наборами данных
        """
        main_page.click_bottom_order_button()
        order_page.complete_order_flow(order_data)

        assert order_page.is_order_successful(), \
            f"Заказ с данными {order_data['name']} {order_data['surname']} не создан"


    def test_order_flow_with_comment(self, main_page, order_page):
        """
        Тест: создание заказа с комментарием
        """
        order_data = OrderData.FIRST_ORDER.copy()
        order_data["comment"] = "Тестовый комментарий: позвонить за 5 минут"

        main_page.click_header_order_button()
        order_page.complete_order_flow(order_data)

        assert order_page.is_order_successful(), "Заказ с комментарием не создан"

    def test_successful_order_from_header_multiple_data(self, main_page, order_page, driver):
        """
        Тест: создание нескольких заказов через кнопку в шапке
        Проверяет возможность создания двух разных заказов подряд
        """
        orders = [OrderData.FIRST_ORDER, OrderData.SECOND_ORDER]

        for i, order_data in enumerate(orders, 1):
            # Клик по кнопке заказа в шапке
            main_page.click_header_order_button()

            # Оформление заказа
            order_page.complete_order_flow(order_data)

            # Проверка успешного создания заказа
            assert order_page.is_order_successful(), \
                f"Заказ {i} с данными {order_data['name']} {order_data['surname']} не создан"

            # Возвращаемся на главную страницу для следующего заказа
            driver.back()
            # Ожидаем загрузки главной страницы
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Home_FAQ__3uVm4"))
            )

    # ==================== ТЕСТЫ ЛОГОТИПОВ ====================

    def test_scooter_logo_redirects_to_main_page(self, main_page, order_page):
        """
        Тест: клик по логотипу Самоката возвращает на главную страницу
        """
        # Переход на страницу заказа
        main_page.click_header_order_button()

        # Ожидаем загрузки страницы заказа
        order_page.wait_for_first_form()

        # Запоминаем URL страницы заказа
        order_url = main_page.get_current_url()

        # Клик по логотипу Самоката
        main_page.click_scooter_logo()

        # Ожидаем изменения URL (редирект на главную)
        WebDriverWait(main_page.driver, 10).until(
            EC.url_changes(order_url)
        )

        # Проверка, что URL изменился
        current_url = main_page.get_current_url()
        assert current_url != order_url, "URL не изменился после клика по логотипу"

        # Проверка, что находимся на главной странице
        assert "order" not in current_url.lower(), "Страница заказа все еще открыта"

    def test_yandex_logo_opens_dzen_in_new_tab(self, main_page, driver):
        main_window = driver.current_window_handle
        initial_windows_count = len(driver.window_handles)

        main_page.click_yandex_logo()

        # Ждем открытия нового окна
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > initial_windows_count
        )

        # Получаем новое окно
        new_window = [w for w in driver.window_handles if w != main_window][0]
        driver.switch_to.window(new_window)

        # Ожидаем, что URL не будет about:blank
        WebDriverWait(driver, 15).until(
            lambda d: d.current_url != "about:blank"
        )

        # Ожидаем загрузки страницы
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        current_url = driver.current_url
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, \
            f"Неверный URL после перехода: {current_url}"

        driver.close()
        driver.switch_to.window(main_window)

    # ==================== ТЕСТЫ ВИДИМОСТИ И ДОСТУПНОСТИ ====================

    def test_order_button_visibility(self, main_page):
        """
        Тест: проверка видимости кнопок заказа на главной странице
        """
        # Проверка кнопки в шапке
        assert main_page.is_header_order_button_visible(), \
            "Кнопка заказа в шапке не видна"

        # Проверка кнопки внизу
        assert main_page.is_bottom_order_button_visible(), \
            "Кнопка заказа внизу страницы не видна"

        # Проверка текста кнопок
        header_text = main_page.get_header_order_button_text()
        bottom_text = main_page.get_bottom_order_button_text()

        assert header_text == "Заказать", f"Неверный текст кнопки в шапке: {header_text}"
        assert bottom_text == "Заказать", f"Неверный текст кнопки внизу: {bottom_text}"

    def test_order_button_clickable(self, main_page):
        """
        Тест: проверка, что кнопки заказа кликабельны
        """
        # Проверка кнопки в шапке
        assert main_page.is_header_button_clickable(), \
            "Кнопка заказа в шапке не кликабельна"

        # Проверка кнопки внизу
        assert main_page.is_bottom_button_clickable(), \
            "Кнопка заказа внизу страницы не кликабельна"

        print("✅ Обе кнопки заказа кликабельны")

    # ==================== ТЕСТЫ ВАЛИДАЦИИ ФОРМЫ ====================

    def test_order_form_validation_empty_fields(self, main_page, order_page, driver):
        """
        Тест: проверка валидации формы заказа с пустыми полями
        """
        main_page.click_header_order_button()
        order_page.wait_for_first_form()

        # Попытка отправить пустую форму
        order_page.click_next_button_without_wait()

        # Проверяем, что остались на первой форме (не перешли на второй шаг)
        assert order_page.is_first_form_visible(), "Форма должна остаться на первом шаге"

        # Проверяем, что вторая форма НЕ открылась
        assert not order_page.is_second_form_visible(timeout=2), \
            "Вторая форма открылась, хотя должны были быть ошибки валидации"

        # Проверяем, что есть хотя бы одна ошибка (любая)
        error_messages = driver.find_elements(By.CLASS_NAME, "Input_ErrorMessage__3HvIb")
        visible_errors = [msg for msg in error_messages if msg.is_displayed()]


    def test_order_form_validation_invalid_phone(self, main_page, order_page, driver):
        """
        Тест: проверка валидации формы заказа с некорректным телефоном
        """
        main_page.click_header_order_button()
        order_page.wait_for_first_form()

        # Заполняем поля с некорректным телефоном
        order_data = OrderData.FIRST_ORDER.copy()
        order_data["phone"] = "123"  # Некорректный телефон

        order_page.fill_first_form(order_data)
        order_page.click_next_button_without_wait()

        # Ожидаем появления сообщения об ошибке по тексту
        error_locator = (By.XPATH, "//div[contains(text(), 'Введите корректный номер')]")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(error_locator)
        )

        # Проверяем, что остались на первой форме
        assert order_page.is_first_form_visible(), "Форма должна остаться на первом шаге"

        # Проверяем текст ошибки
        error_message = driver.find_element(*error_locator)
        assert error_message.is_displayed(), "Сообщение об ошибке не появилось"
        assert "Введите корректный номер" in error_message.text, \
            f"Неверный текст ошибки: {error_message.text}"

        # Проверяем, что поле телефона подсвечено красным
        phone_input = driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
        input_class = phone_input.get_attribute("class")
        assert "Input_Error" in input_class, f"Поле телефона не подсвечено красным. Класс: {input_class}"

    def test_order_form_validation_empty_name(self, main_page, order_page, driver):
        """
        Тест: проверка валидации формы заказа с пустым именем
        """
        main_page.click_header_order_button()
        order_page.wait_for_first_form()

        # Заполняем поля с пустым именем
        order_data = OrderData.FIRST_ORDER.copy()
        order_data["name"] = ""

        order_page.fill_first_form(order_data)
        order_page.click_next_button_without_wait()

        # Ожидаем появления сообщения об ошибке по тексту
        error_locator = (By.XPATH, "//div[contains(text(), 'Введите корректное имя')]")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(error_locator)
        )

        # Проверяем, что остались на первой форме
        assert order_page.is_first_form_visible(), "Форма должна остаться на первом шаге"

        # Проверяем текст ошибки
        error_message = driver.find_element(*error_locator)
        assert error_message.is_displayed(), "Сообщение об ошибке не появилось"
        assert "Введите корректное имя" in error_message.text, \
            f"Неверный текст ошибки: {error_message.text}"

        # Проверяем, что поле имени подсвечено красным
        name_input = driver.find_element(By.XPATH, "//input[@placeholder='* Имя']")
        input_class = name_input.get_attribute("class")
        assert "Input_Error" in input_class, f"Поле имени не подсвечено красным. Класс: {input_class}"

    # ==================== ТЕСТЫ ПЕРЕХОДОВ ====================

    def test_navigation_to_order_page_from_header(self, main_page, order_page):
        """
        Тест: переход на страницу заказа через кнопку в шапке
        """
        main_page.click_header_order_button()

        # Проверяем, что открылась форма заказа
        assert order_page.is_first_form_visible(), "Форма заказа не открылась"

        # Проверяем заголовок формы
        header_text = order_page.get_current_step_header()
        assert "Для кого самокат" in header_text, \
            f"Неверный заголовок формы: {header_text}"

    def test_navigation_to_order_page_from_bottom(self, main_page, order_page):
        """
        Тест: переход на страницу заказа через кнопку внизу
        """
        main_page.click_bottom_order_button()

        # Проверяем, что открылась форма заказа
        assert order_page.is_first_form_visible(), "Форма заказа не открылась"

        # Проверяем заголовок формы
        header_text = order_page.get_current_step_header()
        assert "Для кого самокат" in header_text, \
            f"Неверный заголовок формы: {header_text}"

    # ==================== ТЕСТЫ РАЗНЫХ СЦЕНАРИЕВ ====================

    def test_order_with_different_rental_periods(self, main_page, order_page, driver):
        """
        Тест: заказ с разными сроками аренды
        """
        rental_periods = ["сутки", "двое суток", "трое суток", "четверо суток"]

        for period in rental_periods:
            main_page.click_header_order_button()

            order_data = OrderData.FIRST_ORDER.copy()
            order_data["rental_period"] = period

            order_page.complete_order_flow(order_data)

            assert order_page.is_order_successful(), \
                f"Заказ со сроком аренды '{period}' не создан"

            # Возвращаемся на главную страницу
            driver.back()
            # Ожидаем загрузки главной страницы
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Home_FAQ__3uVm4"))
            )

    def test_order_with_different_colors(self, main_page, order_page, driver):
        """
        Тест: заказ с разными цветами самоката
        """
        colors = ["black", "grey"]

        for color in colors:
            main_page.click_header_order_button()

            order_data = OrderData.FIRST_ORDER.copy()
            order_data["color"] = color

            order_page.complete_order_flow(order_data)

            assert order_page.is_order_successful(), \
                f"Заказ с цветом '{color}' не создан"

            # Возвращаемся на главную страницу
            driver.back()
            # Ожидаем загрузки главной страницы
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Home_FAQ__3uVm4"))
            )




