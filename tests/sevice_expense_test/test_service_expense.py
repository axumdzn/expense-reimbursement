from unittest.mock import MagicMock

from custom_exception.bad_input import BadInput
from dal.expense_dal.expense_dao_imp import ExpenseDAOImp
from entities.expenses import Expense
from service.expenses.expense_imp import ExpenseServiceImp

expense_dao = ExpenseDAOImp()
expense_service = ExpenseServiceImp(expense_dao)


# create expense
def test_service_create_expense_report_wrong_amount():
    try:
        expense = Expense(1, 1005.00, "gas", "travel cost", 1)
        result = expense_service.service_create_expense_report(expense)
        assert False
    except BadInput as e:
        assert str(e) == "Expense amount must be between 1000.00 and 1.00"


def test_service_create_expense_report_wrong_amount_less():
    try:
        expense = Expense(1, 00.50, "gas", "travel cost", 1)
        result = expense_service.service_create_expense_report(expense)
        assert False
    except BadInput as e:
        assert str(e) == "Expense amount must be between 1000.00 and 1.00"


def test_service_create_expense_report_blank_category():
    try:
        expense = Expense(1, 775.00, " ", "travel cost", 1)
        result = expense_service.service_create_expense_report(expense)
        assert False
    except BadInput as e:
        assert str(e) == "Must choose an expense category"


def test_service_create_expense_report_description_too_long():
    try:
        expense = Expense(1, 775.00, "gas", "travelkjldsfhlkawuyegfbajsndvbefjaskvhdfjxkljchvkldsjhcvlkadsjhfgjasdgkfhajksdgaskhdvfjashkvdfjkashvdfjkashvdfcostjlkewrldkjcvlajsdhfgshjdfjshgadfhsjgavdfghjasdvtfhjgadeljgksfgfjsdlkfkgjsdlkjfgsldfjjkglsd", 1)  #need to put in more than 100 characaters"""
        result = expense_service.service_create_expense_report(expense)
        assert False
    except BadInput as e:
        assert str(e) == "Expense description must be 100 characters or less"


def test_service_create_expense_report():
    test = Expense(1,200.0,"gas","ahskljdhfk",3)
    expense_service.expense_dao.create_expense_report = MagicMock(
        return_value=Expense(1, 995.00, "gas", "travel cost", 1))
    expense = expense_service.service_create_expense_report(test)
    assert expense.employee_id == 1


# delete report
def test_delete_expense_report():

    expense_service.expense_dao.delete_expense_report_by_id = MagicMock(
        return_value=True)
    expense = expense_service.service_expense_delete(2)
    assert expense is True


# total amount
def test_get_total_expense_amount():
    expense_service.expense_dao.get_total_expenses_by_id= MagicMock(
        return_value=2000.0
    )
    result = expense_service.service_get_total_expense_by_id(1)
    assert result == 2000.0
