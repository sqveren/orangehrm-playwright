

def test_get_employees(employee_api):
    response = employee_api.get_employees()
    assert response.status == 200