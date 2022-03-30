from abc import ABC, abstractmethod

from entities.expenses import Expense


class ExpenseServiceInterface(ABC):

    @abstractmethod
    def service_create_expense_report(self, expense: Expense) -> Expense:
        pass

    @abstractmethod
    def service_get_total_expense_by_id(self, employee_id: int) -> list[Expense]:
        pass

    @abstractmethod
    def service_expense_delete(self, expense_id: int) -> bool:
        pass
