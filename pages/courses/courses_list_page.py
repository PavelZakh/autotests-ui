from playwright.sync_api import Page

from pages.base_page import BasePage
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.courses.course_view_component import CourseViewComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, identifier='courses-list')
        self.course_view = CourseViewComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)


    def visit_courses_list_page(self) -> None:
        self.visit(self.url)

    def check_visible_empty_view(self) -> None:
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here',
        )
