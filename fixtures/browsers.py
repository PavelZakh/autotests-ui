from typing import Any, Generator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page

BROWSER_STATE_PATH: str = 'browser_state.json'


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Generator[Page, Any, None]:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)


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


@pytest.fixture
def chromium_page_with_state(
        initialize_browser_state: None, request: SubRequest, playwright: Playwright
) -> Generator[Page, Any, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=BROWSER_STATE_PATH
    )
