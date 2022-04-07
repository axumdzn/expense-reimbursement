from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeDAOInterface(ABC):

    @abstractmethod
    def dao_employee_login(self, username, password: str) -> Employee:
        pass
