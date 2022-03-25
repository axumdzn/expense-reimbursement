from custom_exception.bad_input import BadInput
from data_access_layer.employee_data_access.employee_dao_impl import EmployeeDAOImp

employee_dao = EmployeeDAOImp()


def test_dao_employee_login_success():
    username = "Thomas Jefferson"
    password = "password"
    result = employee_dao.dao_employee_login(username, password)
    assert result.username == "Thomas Jefferson"


def test_dao_employee_login_password_wrong():
    try:
        username = "Thomas Jefferson"
        password = "little"
        result = employee_dao.dao_employee_login(username, password)
        assert False
    except BadInput as e:
        assert str(e) != "wrong username or password"
