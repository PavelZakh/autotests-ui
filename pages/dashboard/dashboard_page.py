from playwright.sync_api import Page

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent, ChartIdentifiers, ChartTypes
from tools.routes import AppRoute


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)

        self.students_chart_view = ChartViewComponent(page, ChartIdentifiers.STUDENTS, ChartTypes.BAR)
        self.activities_chart_view = ChartViewComponent(page, ChartIdentifiers.ACTIVITIES, ChartTypes.LINE)
        self.scores_chart_view = ChartViewComponent(page, ChartIdentifiers.SCORES, ChartTypes.SCATTER)
        self.courses_chart_view = ChartViewComponent(page, ChartIdentifiers.COURSES, ChartTypes.PIE)

    def visit_dashboard_page(self) -> None:
        self.visit(AppRoute.DASHBOARD)
