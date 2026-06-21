import pytest
from playwright.sync_api import Playwright, Page

REGISTRATION_URL: str = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
USER_DATA: dict[str, str] = {
    'email': 'user.name@gmail.com',
    'username': 'username',
    'password': 'password',
}
BROWSER_STATE_PATH: str = 'browser_state.json'


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(REGISTRATION_URL)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(USER_DATA['email'])

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(USER_DATA['username'])

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(USER_DATA['password'])

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path=BROWSER_STATE_PATH)


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state: None, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=BROWSER_STATE_PATH)
    # Использую return, т.к. по условию задания возвращаемый тип должен быть Page, а не Generator
    return context.new_page()
