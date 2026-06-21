import pytest
from playwright.sync_api import Page, expect

COURSES_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
DATA_TEST_ID_TEXT_MAPPING = {
    'courses-list-toolbar-title-text': 'Courses',
    'courses-list-empty-view-title-text': 'There is no results',
    'courses-list-empty-view-description-text': 'Results from the load test pipeline will be displayed here',
}


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page) -> None:
    # Переходим на страницу Courses
    chromium_page_with_state.goto(COURSES_URL)

    # Проверяем текстовые поля, их видимость и наличие текста в них
    for data_test_id, text in DATA_TEST_ID_TEXT_MAPPING.items():
        title = chromium_page_with_state.get_by_test_id(data_test_id)
        expect(title).to_be_visible()
        expect(title).to_have_text(text)

    # Отдельно проверяем наличие иконки и ее видимость
    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()
