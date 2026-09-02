

class SideBar:
    def __init__(self, page):
        self.page = page
        self.PIM_page = page.locator("link", name ="PIM")

    def open(self):
        self.page.goto(f"{os.getenv('ORANGEHRM_BASE_URL')}/web/index.php/dashboard")