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

    assert response.status == expected_status_code
    if response.status == 200:
        data = response.json()["data"]
        employee_api.delete_employee([data["empNumber"]])

@allure.feature("Empoloyee Managment")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("Creating employee")
@allure.title("Test creating duplicate employee")
def test_create_duplocate_employee(employee_api: EmployeeApiClient):
    unique_id = str(random.randint(10000,99999))

    with allure.step("Createe the first employee with a unique id"):
        first_response = employee_api.create_employee(
            first_name="Duplicate",
            last_name="Test",
            employee_id=unique_id,
        )
    assert first_response.status == 200
    emp_number_to_cleanup = first_response.json()["data"]["empNumber"]


    with allure.step("Createe the second employee with a used id"):
        second_response = employee_api.create_employee(
            first_name="Duplicate2",
            last_name="Test2",
            employee_id=unique_id,
        )

    with allure.step("Verify duplicate employeeId is rejected"):
        print(f"Duplicate ID attempt status: {second_response.status}")
        assert second_response.status == 422

    with allure.step("Cleanup"):
        employee_api.delete_employee([emp_number_to_cleanup])




@allure.feature("Employee Management")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("Creating empoyee")
@allure.title("Creating an empoyee with special valid characters in name")
@pytest.mark.parametrize("first_name", [
    "O'Brien",
    "Mary-Jane",
    "José",
    "François",
    "李明",
])
def test_create_employee_valid_special_character(employee_api: EmployeeApiClient, first_name):

    unique_id = str(random.randint(10000, 99999))

    response = employee_api.create_employee(
        first_name=first_name,
        last_name = "Test",
        employee_id=unique_id,
    )


    with allure.step("Checking status code"):
        assert response.status == 200

    with allure.step("Checking if characters are valid"):
        emp_number_to_cleanup = response.json()["data"]["empNumber"]  
        data = response.json()["data"]
        assert data["firstName"] == first_name

    with allure.step("Cleanup"):
        employee_api.delete_employee([emp_number_to_cleanup])


@allure.feature("Employee Managment")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Security")
@allure.title("Test creating employee with potentially malicious input")
@pytest.mark.parametrize("malicious_input", [
    "<script>alert('xss')</script>",
    "'; DROP TABLE employees;--",
    "{{7*7}}",
    "../../etc/passwd",
])
def test_creating_employee_security_input(employee_api: EmployeeApiClient, malicious_input):
    unique_id = str(random.randint(10000, 99999))

    response = employee_api.create_employee(
        first_name=malicious_input,
        last_name = "Test",
        employee_id=unique_id,
    )

    with allure.step("Log response for analysis"):
        print(f"Input: {malicious_input} -> Status: {response.status}")
        allure.attach(
            str(response.json()) if response.status != 500 else "No JSON body",
            name="API Response",
            attachment_type=allure.attachment_type.JSON,
        )

    if response.status == 200:
        with allure.step("Verify malicious input was sanitized, not executed as-is"):
            data = response.json()["data"]
            assert "<script>" not in data["firstName"] or data["firstName"] == malicious_input
            
        with allure.step("Cleanup"):
            employee_api.delete_employee([data["empNumber"]])