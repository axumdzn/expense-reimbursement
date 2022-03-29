from unittest.mock import MagicMock

from service.expenses.expense_imp import ExpenseServiceImp

expense_dao = ExpenseDAOImp()
expense_service = ExpenseServiceImp(expense_dao)


def test_create_expense_report():
    expense_service.expense_dao.create_expense_report = MagicMock(return_value=Expense(1, 1005.00, "gas", "travel cost", 1))
    try:
        expense = expense_service.service_create_expense_report(Expense)
        assert expense.employee_id == 1


def test_service_enter_expense_amount_over():
    try:
        expense = Expense(1, 1005.00, "gas", "travel cost", 1)
        expense_service.service_enter_expense_amount(expense)
        assert False
    except BadInput as e:
        assert str(e) == "Expense reimbursement maximum of 1000.00"


def test_service_expense_category_blank():
    try:
        expense = Expense(2, 750.00, "", "travel cost", 1)
        expense_service.service_expense_category(expense)
        assert False
    except BadInput as e:
        assert str(e) == "Cannot leave expense category blank. Please select a matching category."


def test_service_expense_description_long():
    expense_service.service_expense_description = MagicMock(return_value=Expense(101))
    try:
        expense_service.service_expense_description(Expense)
        assert False
    except BadInput as e:
        assert str(e) == "Description too long, must be no longer than 100 characters."


def test_delete_expense_report():
    expense_service.expense_dao.delete_expense_report = MagicMock(return_value=Expense(1, 1005.00, "gas", "travel cost", 1))
    try:
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
