import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
import pytest
from clients.employee_client import EmployeeApiClient

load_dotenv()

@pytest.fixture(scope="session")
def authenticated_state(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    login_page = LoginPage(context.new_page())
    login_page.open()
    login_page.login(os.getenv("ORANGEHRM_USERNAME"), os.getenv("ORANGEHRM_PASSWORD"))

    state = context.storage_state()

    context.close()
    browser.close()
    return state

@pytest.fixture
def logged_in_page(browser, authenticated_state):
    context = browser.new_context(storage_state=authenticated_state)
    page = context.new_page()
    yield page

    context.close()


@pytest.fixture
def employee_api(logged_in_page):
    return EmployeeApiClient(
        request_context=logged_in_page.request, 
        base_url="https://opensource-demo.orangehrmlive.com", 
    )