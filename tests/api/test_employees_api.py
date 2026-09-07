import random
import pytest
import allure
from clients.employee_client import EmployeeApiClient

@allure.feature("Employee Management")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("Get employees")
@allure.title("Test getting employees list")
def test_get_employees(employee_api: EmployeeApiClient):
    response = employee_api.get_employees()
    assert response.status == 200

@allure.feature("Employee Management")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Create employee")
@allure.title("Test creating a new employee")
def test_create_employee(employee_api: EmployeeApiClient):
    with allure.step("Create a new employee"):
        unique_id = str(random.randint(10000, 99999))
        response = employee_api.create_employee(
        first_name="Test",
        last_name="User",
        employee_id= unique_id,
)
    with allure.step("check the response status and data"):
        assert response.status == 200

        data = response.json()["data"]
        assert data["firstName"] == "Test"
        assert data["lastName"] == "User"
        assert "empNumber" in data

@allure.feature("Employee Management")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Update employee")
@allure.title("Test updating an existing employee")
def test_update_employee(employee_api: EmployeeApiClient):
    unique_id = str(random.randint(10000, 99999))
    created_employee_response = employee_api.create_employee(
        first_name="UpdateEmployee",
        last_name="Test1",
        employee_id=unique_id,
    )

    emp_number = created_employee_response.json()["data"]["empNumber"]

    update_response = employee_api.update_employee(
        emp_number=emp_number,
        first_name="Updated",
        last_name="Test1",    
        employee_id=unique_id,  
    )

    assert update_response.status == 200
    assert update_response.json()["data"]["firstName"] == "Updated"

    employee_api.delete_employee([emp_number])

@allure.feature("Employee Management")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Create employee")
@allure.title("Create employee with valid data")
@pytest.mark.parametrize("first_name, last_name", [
    ("John", "Doe"),
    ("Jane", "Smith"),
    ("Alice", "Johnson"),
    ("Bob", "Brown"),
    ("Charlie", "Davis")
   ])
def test_create_employee_parametrized(employee_api: EmployeeApiClient, first_name, last_name):
    unique_id = str(random.randint(10000, 99999))
    response = employee_api.create_employee(
        first_name=first_name,
        last_name=last_name,
        employee_id=unique_id,
    )

    assert response.status == 200

    data = response.json()["data"]
    assert data["firstName"] == first_name
    assert data["lastName"] == last_name
    assert "empNumber" in data

    employee_api.delete_employee([data["empNumber"]])

@allure.feature("Employee Management")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("Create employee")
@allure.title("Test creating employee with edge case first names")
@pytest.mark.parametrize("first_name, expected_status_code",[
    ("A"*29, 200),
    ("A" * 30,200 ),
    ("A" * 31, 422),
    (" ", 422),
    ("A", 200),
   ])
def test_create_employee_edge_cases(employee_api: EmployeeApiClient, first_name, expected_status_code):
    unique_id = str(random.randint(10000, 99999))
    response = employee_api.create_employee(
        first_name=first_name,
        last_name="Test",
        employee_id=unique_id,
    )
    print(f"Input length {len(first_name)}: '{first_name[:20]}...' -> Status: {response.status}")

    if response.status == 200:
        data = response.json()["data"]
        employee_api.delete_employee([data["empNumber"]])


# @pytest.mark.parametrize("last_name", [
#     "A" * 10,
#     "A" * 30,
#     "A" * 31,
#     "A" * 32,
#     "A" * 33,
# ])
# def test_find_exact_length_boundary(employee_api, last_name):
#     unique_id = str(random.randint(10000, 99999))
#     response = employee_api.create_employee(
#         first_name="test",
#         last_name=last_name,
#         employee_id=unique_id,
#     )
#     print(f"Length {len(last_name)}: Status {response.status}")
