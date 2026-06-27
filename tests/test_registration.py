import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage) -> None:
    registration_page.visit_registration_page()
    registration_page.fill_registration_form(
        email="user.name@gmail.com", username="username", password="password"
    )
    registration_page.click_registration_button()

    dashboard_page.check_visible_dashboard_title()
