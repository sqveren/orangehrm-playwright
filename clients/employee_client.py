from clients.base_client import BaseApiClient


class EmployeeApiClient(BaseApiClient):
    ENDPOINT = "/web/index.php/api/v2/pim/employees"


    def get_employees(self, limit=50, offset=0, sort_field="employee.firstName", sort_order="ASC"):
        params = {
            "limit": limit,
            "offset": offset,
            "model": "detailed",
            "includeEmployees": "onlyCurrent",
            "sortField": sort_field,
            "sortOrder": sort_order,
        }
        return self.get(self.ENDPOINT, params=params)
    

    def create_employee(self, first_name, last_name, middle_name="", employee_id="", emp_picture=None):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "employeeId": employee_id,
        }

        return self.post(self.ENDPOINT, data = payload)