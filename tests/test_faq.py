import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.pages.main_page.main_page_locators import MainPageLocators
from src.data.faq_data import FAQ_DATA


class TestFAQ:

    def test_faq_section_visibility(self, main_page):
        """Тест: Проверка видимости раздела FAQ"""
        assert main_page.is_faq_section_visible(), "Раздел FAQ не отображается на странице"

    def test_faq_header_text(self, main_page):
        """Тест: Проверка текста заголовка FAQ"""
        header_text = main_page.get_faq_header_text()
        assert header_text == "Вопросы о важном", \
            f"Заголовок FAQ: '{header_text}', ожидалось 'Вопросы о важном'"

    def test_all_questions_count(self, main_page):
        """Тест: Проверка количества вопросов"""
        questions = main_page.get_questions()
        assert len(questions) == len(FAQ_DATA), \
            f"Найдено {len(questions)} вопросов, ожидалось {len(FAQ_DATA)}"

    def test_all_questions_are_visible(self, main_page):
        """Тест: Проверка видимости всех вопросов"""
        questions = main_page.get_questions()
        for i, question in enumerate(questions):
            assert question.is_displayed(), f"Вопрос {i} не отображается на странице"

    @pytest.mark.parametrize("index,question_text,expected_answer", FAQ_DATA)
    def test_faq_accordion_by_index(self, main_page, driver, index, question_text, expected_answer):
        """
        Тест: Проверка работы аккордеона (по индексу)
        Шаги:
        1. Убедиться, что ответ изначально скрыт
        2. Кликнуть на вопрос
        3. Проверить, что ответ стал видимым
        4. Проверить текст ответа
        """
        # Шаг 1: Проверяем, что ответ изначально не виден
        assert not main_page.is_answer_visible_by_index(index), \
            f"Ответ на вопрос '{question_text}' изначально отображается"

        # Шаг 2: Кликаем на вопрос
        main_page.click_question_by_index(index)

        # Шаг 3: Ждем появления ответа
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(MainPageLocators.get_answer_by_index(index))
            )
        except TimeoutException:
            pytest.fail(f"Ответ на вопрос '{question_text}' не появился после клика")

        # Шаг 4: Проверяем, что ответ стал видимым
        assert main_page.is_answer_visible_by_index(index), \
            f"Ответ на вопрос '{question_text}' не отобразился после клика"

        # Шаг 5: Проверяем текст ответа
        actual_answer = main_page.get_answer_text_by_index(index)
        assert actual_answer == expected_answer, \
            f"Текст ответа не совпадает.\nОжидалось: {expected_answer}\nПолучено: {actual_answer}"

    def test_only_one_answer_open_at_time(self, main_page, driver):
        """
        Тест: Проверка, что открывается только один ответ за раз
        Шаги:
        1. Открыть первый вопрос
        2. Убедиться, что открыт только первый ответ
        3. Открыть второй вопрос
        4. Убедиться, что теперь открыт только второй ответ, а первый закрылся
        """
        # Открываем первый вопрос
        main_page.click_question_by_index(0)

        # Ждем появления первого ответа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.get_answer_by_index(0))
        )

        # Проверяем, что открыт только первый ответ
        assert main_page.is_answer_visible_by_index(0), "Первый ответ должен быть открыт"
        for i in range(1, len(FAQ_DATA)):
            assert not main_page.is_answer_visible_by_index(i), f"Ответ {i} не должен быть открыт"

        # Открываем второй вопрос
        main_page.click_question_by_index(1)

        # Ждем появления второго ответа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.get_answer_by_index(1))
        )

        # Проверяем, что первый закрылся, второй открылся
        assert not main_page.is_answer_visible_by_index(0), "Первый ответ должен закрыться"
        assert main_page.is_answer_visible_by_index(1), "Второй ответ должен открыться"

    def test_click_same_question_twice(self, main_page, driver):
        """
        Тест: Проверка поведения при повторном клике на один и тот же вопрос
        Ожидаемое поведение: ответ остается открытым (аккордеон не закрывается)
        """
        # Первый клик - открываем
        main_page.click_question_by_index(0)

        # Ждем появления ответа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.get_answer_by_index(0))
        )
        assert main_page.is_answer_visible_by_index(0), "Ответ должен открыться после первого клика"

        # Второй клик - по логике аккордеона ответ должен остаться открытым
        main_page.click_question_by_index(0)

        # Проверяем, что ответ все еще видим
        assert main_page.is_answer_visible_by_index(0), "Ответ должен остаться открытым после повторного клика"

    def test_all_answers_have_text(self, main_page, driver):
        """
        Тест: Проверка, что все ответы содержат текст
        Шаги:
        1. Открыть каждый вопрос по очереди
        2. Проверить, что текст ответа не пустой
        """
        for i, (_, question_text, expected_answer) in enumerate(FAQ_DATA):
            # Открываем вопрос
            main_page.click_question_by_index(i)

            # Ждем появления ответа
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(MainPageLocators.get_answer_by_index(i))
            )

            # Получаем текст ответа
            answer_text = main_page.get_answer_text_by_index(i)

            # Проверяем, что текст не пустой
            assert answer_text, f"Ответ на вопрос {i} ('{question_text}') пустой"
            assert len(answer_text) > 0, f"Ответ на вопрос {i} не содержит текста"

            # Проверяем соответствие ожидаемому тексту
            assert answer_text == expected_answer, \
                f"Текст ответа на вопрос {i} не соответствует ожидаемому"

    def test_questions_have_correct_texts(self, main_page):
        """
        Тест: Проверка, что тексты вопросов соответствуют ожидаемым
        """
        questions = main_page.get_questions()
        for i, question in enumerate(questions):
            expected_question = FAQ_DATA[i][1]
            actual_question = question.text.strip()
            assert actual_question == expected_question, \
                f"Текст вопроса {i} не совпадает.\nОжидалось: {expected_question}\nПолучено: {actual_question}"