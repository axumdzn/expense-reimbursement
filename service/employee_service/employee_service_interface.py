from abc import ABC, abstractmethod

from custom_exception.bad_input import BadInput
from entities.employee import Employee


class EmployeeServiceInterface(ABC):

    @abstractmethod
    def service_employee_login(self, username, password) -> Employee:
        pass

