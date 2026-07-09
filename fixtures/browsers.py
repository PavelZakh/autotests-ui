from typing import Any, Generator

import pytest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage

BROWSER_STATE_PATH: str = 'browser_state.json'


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit_registration_page()

    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()

    context.storage_state(path=BROWSER_STATE_PATH)
    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state: None, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=BROWSER_STATE_PATH)
    # Использую return, т.к. по условию задания возвращаемый тип должен быть Page, а не Generator
    return context.new_page()
