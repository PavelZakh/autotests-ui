import pytest

from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page_with_state: CoursesListPage) -> None:
    courses_list_page_with_state.visit_courses_list_page()

    courses_list_page_with_state.sidebar.check_visible()
    courses_list_page_with_state.navbar.check_visible("username")

    courses_list_page_with_state.toolbar_view.check_visible()

    courses_list_page_with_state.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(
        create_course_page_with_state: CreateCoursePage, courses_list_page_with_state: CoursesListPage
) -> None:
    create_course_page_with_state.visit_create_course_page()

    create_course_page_with_state.check_visible_create_course_title()
    create_course_page_with_state.check_disabled_create_course_button()

    create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=False)

    create_course_page_with_state.check_visible_create_course_form(
        title='', estimated_time='', description='', max_score='0', min_score='0'
    )

    create_course_page_with_state.check_visible_exercises_title()
    create_course_page_with_state.check_visible_create_exercise_button()
    create_course_page_with_state.check_visible_exercises_empty_view()

    create_course_page_with_state.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=True)

    create_course_page_with_state.fill_create_course_form(
        title='Playwright',
        estimated_time='2 weeks',
        description='Playwright',
        max_score='100',
        min_score='10',
    )
    create_course_page_with_state.click_create_course_button()

    courses_list_page_with_state.toolbar_view.check_visible()
    courses_list_page_with_state.course_view.check_visible(
        index=0, title='Playwright', max_score='100', min_score='10', estimated_time='2 weeks'
    )
