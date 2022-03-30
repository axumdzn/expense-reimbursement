from unittest.mock import MagicMock

from custom_exception.bad_input import BadInput
from entities.expenses import Expense
from service.expenses.expense_imp import ExpenseServiceImp

expense_service = ExpenseServiceImp()


def test_service_create_expense_report_wrong_amount():
    try:
        expense_service.service_create_expense_report = (1, 1005.00, "gas", "travel cost", 1)
        result = expense_service.service_create_expense_report(Expense)
        assert False
    except BadInput as e:
        assert str(e) == "Expense amount must be between 1000.00 and 1.00"


def test_service_create_expense_report_wrong_amount_less():
    try:
        expense_service.service_create_expense_report = (1, 00.50, "gas", "travel cost", 1)
        result = expense_service.service_create_expense_report(Expense)
        assert False
    except BadInput as e:
        assert str(e) == "Expense amount must be between 1000.00 and 1.00"


def test_service_create_expense_report_blank_category():
    try:
        expense_service.service_create_expense_report = (1, 775.00, " ", "travel cost", 1)
        result = expense_service.service_create_expense_report(Expense)
        assert False
    except BadInput as e:
        assert str(e) == "Must choose an expense category"

def test_service_create_expense_report_description_too_long():
    try:
        expense_service.service_create_expense_report = (1, 775.00, "gas", "travel cost", 1)  #need to put in more than 100 characaters"""
        result = expense_service.service_create_expense_report(Expense)
        assert False
    except BadInput as e:
        assert str(e) == "Expense description must be 100 characters or less"


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
