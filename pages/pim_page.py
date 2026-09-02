

class PimPage:
    def __init__(self, page):
        self.page = page
        self.employee_name_input = page.get_by_placeholder("Type for hints...").nth(0)
        self.supervisor_name_input = page.get_by_placeholder("Type for hints...").nth(1)
        
        self.employee_id = page.locator("div.oxd-input-group").filter(has_text="Employee Id").locator("input")
        
        self.employment_status_dropdown = self._dropdown_by_label("Employment Status")
        self.include_dropdown = self._dropdown_by_label("Include")
        self.job_title_dropdown = self._dropdown_by_label("Job Title")
        self.sub_unit_dropdown = self._dropdown_by_label("Sub Unit")
        self.button_search = page.get_by_role("button", name="Search")
        self.button_reset = page.get_by_role("button", name="reset")


    def _dropdown_by_label(self, label: str):
        return (
            self.page.locator("div.oxd-input-group")
            .filter(has_text=label)
            .locator(".oxd-select-text-input")
        )
        
    def open(self):
        self.page.goto(f"{os.getenv('ORANGEHRM_BASE_URL')}/web/index.php/pim/viewPimModule")

    def select_employment_status(self, status):
        self.employment_status_dropdown.click()
        self.page.get_by_role("option", name=status).click()

    def select_include(self, include_option):  
        self.include_dropdown.click()
        self.page.get_by_role("option", name=include_option).click()

    def select_job_title(self, job_title):
        self.job_title_dropdown.click()
        self.page.get_by_role("option", name=job_title).click()

    def select_sub_unit(self, sub_unit):
        self.sub_unit_dropdown.click()
        self.page.get_by_role("option", name=sub_unit).click()
