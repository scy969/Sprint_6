import allure
import pytest
from data import faq_test_data, faq_test_ids


@allure.epic("Сервис аренды самокатов")
@allure.feature("Раздел 'Вопросы о важном' (FAQ)")
class TestFaq:

    @allure.title("Тест вопросов FAQ")
    @allure.description("Проверка, что при клике на вопрос открывается правильный ответ")
    @pytest.mark.parametrize("faq_item", faq_test_data, ids=faq_test_ids)
    def test_faq_questions(self, main_page, faq_item):
        # Используем метод из BasePage вместо прямого обращения к driver
        main_page.open_main_page()
        main_page.close_cookie_banner()
        main_page.click_faq_question_safe(faq_item["question_locator"])
        answer_text = main_page.get_faq_answer_text(faq_item["answer_locator"])

        with allure.step(f"Проверить, что ответ содержит '{faq_item['expected_text']}'"):
            assert faq_item["expected_text"] in answer_text