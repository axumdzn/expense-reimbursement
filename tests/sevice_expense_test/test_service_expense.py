from unittest.mock import MagicMock

from entities.expenses import Expense
from service.expenses.expense_imp import ExpenseServiceImp


expense_service = ExpenseServiceImp()


def test_service_create_expense_report():
    expense_service.expense_dao.create_expense_report = MagicMock(
        return_value=Expense(1, 995.00, "gas", "travel cost", 1))
    expense = expense_service.service_create_expense_report(Expense)
    assert expense.employee_id == 1


def test_delete_expense_report():
    expense_service.expense_dao.delete_expense_report = MagicMock(
        return_value=Expense(1, 995.00, "gas", "travel cost", 1))
    expense = expense_service.service_expense_delete(Expense)
    assert expense.expense_id == 1


def test_get_total_expense_amount():
    expense_service.expense_dao.select_all_total_expense_by_id = MagicMock(
        return_value=[
            Expense(1, 750.00, "gas", "travel cost", 1),
            Expense(2, 550.00, "gas", "travel cost", 1)
        ]
    )
    result = expense_service.service_get_total_expense_by_id(1)
    assert len(result) == 2
