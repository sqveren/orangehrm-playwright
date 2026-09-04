

def test_get_employees(employee_api):
    response = employee_api.get_employees()
    assert response.status == 200


def test_create_employee(employee_api):
    response = employee_api.create_employee(
    first_name="Test",
    last_name="User",
    employee_id="99999",
    )
    
    assert response.status == 200

    data = response.json()["data"]
    assert data["firstName"] == "Test"
    assert data["lastName"] == "User"
    assert "empNumber" in data