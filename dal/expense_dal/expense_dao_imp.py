from dal.expense_dal.expense_dao_interface import ExpenseDAOInterface
from entities.employee import Employee
from entities.expenses import Expense


class ExpenseDAOImp(ExpenseDAOInterface):

    def create_expense_report(self, expense: Expense) -> Expense:
        sql = "insert into employees values(%s, %s, %s, %s, %s) returning expense_id"
        cursor = connection.cursor()
        cursor.execute(sql,(expense.expense_id, expense.amount, expense.category, expense.description, expense.employee_id))
        connection.commit()
        returned_id = cursor.fetchone()[0]
        expense.employee_id = returned_id
        return expense

    def delete_expense_report_by_id(self, expense: Expense) -> Expense:
        sql = "insert into employees values(%s, %s, %s, %s, %s) returning expense_id"
        cursor = connection.cursor()
        cursor.execute(sql,(expense.expense_id, expense.amount, expense.category, expense.description, expense.employee_id))
        connection.commit()
        # returned_id = cursor.fetchone()[0]
        # expense.employee_id = returned_id
        return expense
