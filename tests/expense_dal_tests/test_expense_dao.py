from custom_exception.bad_input import BadInput
from dal.expense_dal.expense_dao_imp import ExpenseDAOImp
from entities.expenses import Expense

expense_dao = ExpenseDAOImp()


# Test that employees can see the total amount of money they have requested
# Test to create expense report
# Test to cancel expense request

def test_create_expense_report_success():
    expense = Expense(1, 2.2, "gas", "Comment", 1)
    result_expense = expense_dao.create_expense_report(expense)
    assert result_expense.employee_id == 1


def test_create_expense_report_failure():
    try:
        expense = Expense(1, "john", "gas", "Comment", 1)
        result_expense = expense_dao.create_expense_report(expense)
        assert False
    except BadInput as e:
        assert str(e) == "Invalid information entered"


def test_get_total_expenses_by_id_success():
    result_expense = expense_dao.get_total_expenses_by_id(1)
    assert result_expense == 1000


def test_get_total_expenses_by_id_failure():
    try:
        result_expense = expense_dao.get_total_expenses_by_id(-10)
        assert False
    except BadInput as e:
        assert str(e) == "This user does not exist"


def test_delete_expense_report_success():
    expense = Expense(1, 2.2, "gas", "Comment", 1)
    result_expense = expense_dao.delete_expense_report(expense)
    assert result_expense.employee_id == 1


def test_delete_expense_report_failure():
    try:
        expense = Expense(1, "john", "mileage", "Comment", 1)
        result_expense = expense_dao.delete_expense_report(expense)
        assert False
    except BadInput as e:
        assert str(e) == "Invalid information entered"
