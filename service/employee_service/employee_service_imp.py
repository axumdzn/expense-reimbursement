from custom_exception.bad_input import BadInput
from dal.employee_data_access.employee_dao_impl import EmployeeDAOImp
from entities.employee import Employee
from service.employee_service.employee_service_interface import EmployeeServiceInterface


class EmployeeServiceImp(EmployeeServiceInterface):

    def __init__(self, employee_dao: EmployeeDAOImp):
        self.employee_dao = employee_dao

    def service_employee_login(self, username, password) -> Employee:
        if type(username) is not str:
            raise BadInput("Wrong type of input entered for username or password")
        if type(password) is not str:
            raise BadInput("Wrong type of input entered for username or password")
        return self.employee_dao.dao_employee_login(username, password)
