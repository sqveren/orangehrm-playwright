from pages.pim_page import PimPage
from playwright.sync_api import expect
import random

def test_search_employee_by_name(logged_in_page, employee_api):
    unique_id = str(random.randint(10000, 99999))
    create_response = employee_api.create_employee(
        first_name="UniqueSearchTest",
        last_name="Employee",
        employee_id=unique_id,
    )
    emp_number = create_response.json()["data"]["empNumber"]

    pim_page = PimPage(logged_in_page)
    pim_page.open()
    pim_page.fill_employee_info(employee_name="UniqueSearchTest")
    pim_page.button_search.click()

    expect(pim_page.result_rows).to_have_count(1)

    employee_api.delete_employee([emp_number])