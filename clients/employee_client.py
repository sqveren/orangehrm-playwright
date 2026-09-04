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
    

    def update_employee(self,
        emp_number,
        first_name="",
        last_name="",
        middle_name="",
        employee_id="",
        other_id="",
        driving_license_no="",
        driving_license_expired_date=None,
        nationality_id=None,
        gender=None,
        birthday=None,):
    
        payload = {
        "firstName": first_name,
        "lastName": last_name,
        "middleName": middle_name,
        "employeeId": employee_id,
        "otherId": other_id,
        "drivingLicenseNo": driving_license_no,
        "drivingLicenseExpiredDate": driving_license_expired_date,
        "nationalityId": nationality_id,
        "gender": gender,
        "birthday": birthday,
    }
        endpoint = f"{self.ENDPOINT}/{emp_number}/personal-details"
        return self.put(endpoint, data=payload)
    
    def delete_employee(self, emp_numbers: list):
        payload = {
        "ids": emp_numbers,
        }

        return self.delete(self.ENDPOINT, data=payload)
    