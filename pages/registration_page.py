from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id("registration-page-registration-button")
        self.login_link = page.get_by_test_id("registration-page-login-link")

    def visit_registration_page(self) -> None:
        self.visit(self.url)

    def click_registration_button(self) -> None:
        self.registration_button.click()

    def click_login_link(self) -> None:
        self.login_link.click()
