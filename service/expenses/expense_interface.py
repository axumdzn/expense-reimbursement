from abc import ABC, abstractmethod


class ExpenseServiceInterface(ABC):

    def __int__(self, expense_dao: ExpenseDAOInterface):
        self.expense_dao = expense_dao

    @abstractmethod
    def service_create_expense_report(self, expense: Expense) -> Expense:
        pass

    @abstractmethod
    def service_enter_expense_amount(self, amount: float) -> Expense:
        pass

    @abstractmethod
    def service_get_total_expense_by_id(self, employee_id: int) -> list[Expense]:
        pass

    @abstractmethod
    def service_expense_category(self, category: str) -> bool:
        pass

    @abstractmethod
    def service_expense_description(self, description: str) -> bool:
        pass

    @abstractmethod
    def service_expense_delete(self, employee_id: int) -> bool:
        pass
