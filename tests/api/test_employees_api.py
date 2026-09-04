import random

def test_get_employees(employee_api):
    response = employee_api.get_employees()
    assert response.status == 200


def test_create_employee(employee_api):
    unique_id = str(random.randint(10000, 99999))
    response = employee_api.create_employee(
    first_name="Test",
    last_name="User",
    employee_id= unique_id,
    )
    
    assert response.status == 200

    data = response.json()["data"]
    assert data["firstName"] == "Test"
    assert data["lastName"] == "User"
    assert "empNumber" in data


    

def test_update_employee(employee_api):
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
