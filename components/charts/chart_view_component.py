from enum import StrEnum

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartIdentifiers(StrEnum):
    """
    Класс с идентификаторами чартов.
    """
    STUDENTS = 'students'
    ACTIVITIES = 'activities'
    COURSES = 'courses'
    SCORES = 'scores'


class ChartTypes(StrEnum):
    """
    Класс с типами чартов.
    """
    BAR = 'bar'
    LINE = 'line'
    PIE = 'pie'
    SCATTER = 'scatter'


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: ChartIdentifiers, chart_type: ChartTypes):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible "{title}" chart')
    def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()
