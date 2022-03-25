from abc import ABC, abstractmethod

from entities.expenses import Expense


class ExpenseDAOInterface(ABC):

    @abstractmethod
    def create_expense_report(self, expense: Expense) -> Expense:
        pass

    @abstractmethod
    def delete_expense_report_by_id(self, expense_id: int) -> bool:
        pass

    @abstractmethod
    def get_total_expenses_by_id(self, employee_id: int) -> float:
        pass
