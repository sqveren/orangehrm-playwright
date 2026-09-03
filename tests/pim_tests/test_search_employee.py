from pages.pim_page import PimPage
from playwright.sync_api import expect

def test_search_employee_by_name(logged_in_page):
    pim_page = PimPage(logged_in_page)
    pim_page.open()
    
    pim_page.fill_employee_info(employee_name="Joy Smith")
    pim_page.button_search.click()

    expected_count = pim_page.get_records_found_number()
    expect(pim_page.result_rows).to_have_count(expected_count)