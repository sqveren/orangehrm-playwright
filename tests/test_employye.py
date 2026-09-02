def test_employee(logged_in_page):
    page = logged_in_page

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

    locator = (
        page.locator("div.oxd-input-group")
        .filter(has_text="Employee Id")
        .locator("input")
    )

    locator.first.wait_for(state="visible")
    print("Кількість:", locator.count())