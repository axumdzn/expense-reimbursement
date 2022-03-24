from entities.employee import Employee
from service.employee_service.employee_service_interface import EmployeeServiceInterface


class EmployeeServiceImp(EmployeeServiceInterface):

    def service_employee_login(self, username, password) -> Employee:
        pass
