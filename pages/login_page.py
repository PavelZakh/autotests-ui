from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

        self.login_form = LoginFormComponent(page)

        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def visit_login_page(self) -> None:
        self.visit(self.url)

    def click_login_button(self) -> None:
        self.login_button.click()

    def click_registration_link(self) -> None:
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self) -> None:
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")
