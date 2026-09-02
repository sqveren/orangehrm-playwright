import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
import pytest

load_dotenv()


@pytest.fixture
def logged_in_page(page):

    login_page = LoginPage(page)

    login_page.open()
    login_page.login(os.getenv("ORANGEHRM_USERNAME"), os.getenv("ORANGEHRM_PASSWORD"))

    return page