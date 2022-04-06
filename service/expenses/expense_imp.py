from custom_exception.bad_input import BadInput
from dal.expense_dal.expense_dao_imp import ExpenseDAOImp
from entities.expenses import Expense
from service.expenses.expense_interface import ExpenseServiceInterface


class ExpenseServiceImp(ExpenseServiceInterface):

    def __init__(self, expense_dao: ExpenseDAOImp):
        self.expense_dao = expense_dao

    def service_create_expense_report(self, expense: Expense) -> Expense:
        if type(expense.amount) is not float:
            raise BadInput("Enter numerical digits between 1.00 and 1000.00")
        elif type(expense.category) is not str:
            raise BadInput("Must choose an expense category")
        elif type(expense.description) is not str:
            raise BadInput("Expense description must be 100 characters or less")
        elif expense.amount > 1000.0 or expense.amount < 1.0:
            raise BadInput("Expense amount must be between 1000.00 and 1.00")
        elif expense.category == " ":
            raise BadInput("Must choose an expense category")
        elif len(expense.description) > 100:
            raise BadInput("Expense description must be 100 characters or less")
        return self.expense_dao.create_expense_report(expense)

    def service_get_total_expense_by_id(self, employee_id: int) -> float:
        if type(employee_id) is not int:
            raise BadInput("Please enter valid employee ID")
        return self.expense_dao.get_total_expenses_by_id(employee_id)

    def service_expense_delete(self, expense_id: int) -> bool:
        if type(expense_id) is not int:
            raise BadInput("Please enter valid employee ID")
        return self.expense_dao.delete_expense_report_by_id(expense_id)