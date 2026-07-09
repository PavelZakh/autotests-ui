import pytest

from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page_with_state: CoursesListPage) -> None:
        courses_list_page_with_state.visit_courses_list_page()

        courses_list_page_with_state.sidebar.check_visible()
        courses_list_page_with_state.navbar.check_visible("username")

        courses_list_page_with_state.toolbar_view.check_visible()

        courses_list_page_with_state.check_visible_empty_view()


    def test_create_course(
            self, create_course_page_with_state: CreateCoursePage, courses_list_page_with_state: CoursesListPage
    ) -> None:
        create_course_page_with_state.visit_create_course_page()

        create_course_page_with_state.create_course_toolbar_view.check_visible()

        create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=False)

        create_course_page_with_state.create_course_form.check_visible()

        create_course_page_with_state.create_course_exercises_toolbar_view.check_visible()

        create_course_page_with_state.check_visible_exercises_empty_view()

        create_course_page_with_state.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page_with_state.create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10',
        )
        create_course_page_with_state.create_course_toolbar_view.click_create_button()

        courses_list_page_with_state.toolbar_view.check_visible()
        courses_list_page_with_state.course_view.check_visible(
            index=0, title='Playwright', max_score='100', min_score='10', estimated_time='2 weeks'
        )

    def test_edit_course(
            self, create_course_page_with_state: CreateCoursePage, courses_list_page_with_state: CoursesListPage
    ) -> None:
        create_course_page_with_state.visit_create_course_page()

        create_course_page_with_state.create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10',
        )

        create_course_page_with_state.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page_with_state.create_course_toolbar_view.click_create_button()


        courses_list_page_with_state.course_view.check_visible(
            index=0, title='Playwright', max_score='100', min_score='10', estimated_time='2 weeks',
        )

        courses_list_page_with_state.course_view.menu.click_edit(index=0)

        create_course_page_with_state.create_course_form.fill(
            title='Selenium',
            estimated_time='10 years',
            description='Selenium',
            max_score='20',
            min_score='2',
        )
        create_course_page_with_state.create_course_toolbar_view.click_create_button()

        courses_list_page_with_state.course_view.check_visible(
            index=0, title='Selenium', max_score='20', min_score='2', estimated_time='10 years',
        )
