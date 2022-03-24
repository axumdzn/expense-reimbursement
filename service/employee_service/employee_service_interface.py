from abc import ABC, abstractmethod

from custom_exception.bad_input import BadInput
from entities.employee import Employee


class EmployeeServiceInterface(ABC):

    def __init__(self, employee_dao):
        self.employee_dao = employee_dao

    @abstractmethod
    def service_employee_login(self, username, password) -> Employee:
        if type(username) is not str:
            raise BadInput("Wrong type of input entered for username or password")
        if type(password) is not str:
            raise BadInput("Wrong type of input entered for username or password")
        return self.employee_dao.employee_login(username, password)

