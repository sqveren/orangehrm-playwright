

class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.dashboard_header = page.get_by_role("heading", name="Dashboard")
        self.timesheet = page.get_by_title("Timesheets")
        self.my_timesheet = page.get_by_title("My Timesheet")
        self.candidates_to_interweview = page.locator("oxd-text oxd-text--p", has_text="Candidate to Interview")
        self.pending_self_reviewpage = page.locator("p.oxd-text.oxd-text--p", has_text="Pending Self Review")
        

    def is_dashboard_visible(self):
        return self.dashboard_header.is_visible()
    
