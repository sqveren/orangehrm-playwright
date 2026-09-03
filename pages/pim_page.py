import os

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

        self.result_rows = page.locator(".oxd-table-body .oxd-table-card")
        self.records_found_text = page.locator("text=Records Found")


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

    def fill_employee_info(self,employee_name=None,supervisor_name=None,employee_id=None,employment_status=None,include_option=None,job_title=None,sub_unit=None,):
        
        if employee_name:
            self.employee_name_input.fill(employee_name)
        if supervisor_name:
            self.supervisor_name_input.fill(supervisor_name)
        if employee_id:
            self.employee_id.fill(employee_id)
        if employment_status:
            self.select_employment_status(employment_status)
        if include_option:
            self.select_include(include_option)
        if job_title:
            self.select_job_title(job_title)
        if sub_unit:
            self.select_sub_unit(sub_unit)

    
    def get_results_count(self):
        return self.result_rows.count()

    def get_records_found_number(self) -> int:
        text = self.records_found_text.inner_text()  
        number_part = text.split(")")[0]              
        return int(number_part.strip("("))  