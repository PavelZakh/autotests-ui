from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")

    context.storage_state(path='browser_state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser_state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    data_test_id_text_mapping = {
        'courses-list-toolbar-title-text': 'Courses',
        'courses-list-empty-view-title-text': 'There is no results',
        'courses-list-empty-view-description-text': 'Results from the load test pipeline will be displayed here',
    }

    # Проверяем текстовые поля, их видимость и наличие текста в них
    for data_test_id, text in data_test_id_text_mapping.items():
        title = page.get_by_test_id(data_test_id)
        expect(title).to_be_visible()
        expect(title).to_have_text(text)

    # Отдельно проверяем наличие иконки и ее видимость
    empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()
