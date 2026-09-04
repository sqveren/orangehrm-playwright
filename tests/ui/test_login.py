from playwright.sync_api import Page, expect


def test_login(logged_in_page: Page):
    logged_in_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    expect(logged_in_page).to_have_url(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )
    expect(
        logged_in_page.get_by_role("heading", name="Dashboard")
    ).to_be_visible()