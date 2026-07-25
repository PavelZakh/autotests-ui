import re

from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from tools.routes import AppRoute


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, "registration-page-registration-button", "Registration")
        self.login_link = Link(page, "registration-page-login-link", "Login")

    def visit_registration_page(self) -> None:
        self.visit(AppRoute.REGISTRATION)

    def click_registration_button(self) -> None:
        self.registration_button.click()

    def click_login_link(self) -> None:
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))
