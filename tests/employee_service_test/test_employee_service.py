from unittest.mock import MagicMock

from custom_exception.bad_input import BadInput
from entities.employee import Employee
from service.employee_service.employee_service_imp import EmployeeServiceImp

employee_service = EmployeeServiceImp()


def test_service_employee_login_success():
    username = "joejoe"
    password = "password"
    result = employee_service.service_employee_login(username,password)
    assert result.name == "Joe"


def test_service_employee_login_username_not_string():
    try:
        username = 4
        password = "password"
        result = employee_service.service_employee_login(username, password)
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered for username or password"


def test_service_employee_login_password_not_string():
    try:
        username = "joejoe"
        password = 4
        result = employee_service.service_employee_login(username, password)
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered for username or password"


def test_service_employee_login_mock_success():
    employee_service.service_employee_login.employee_login = MagicMock(return_value=Employee(1, "Joe", "Smith", "joejoe", "password"))
    result = employee_service.service_employee_login("joecool", "hasta_la_pasta")
    assert result.username == "joejoe"


# will write when the completed version of the employee dao is written completely
def test_service_employee_login_mock_failure():
    pass
