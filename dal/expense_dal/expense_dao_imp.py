from custom_exception.bad_input import BadInput
from dal.expense_dal.expense_dao_interface import ExpenseDAOInterface
from entities.expenses import Expense
from util.manage_connection import connection


class ExpenseDAOImp(ExpenseDAOInterface):

    def create_expense_report(self, expense: Expense) -> Expense:
        sql = "insert into expenses values(%s, %s, %s, %s, %s) returning expense_id"
        cursor = connection.cursor()
        cursor.execute(sql, (expense.expense_id, expense.amount, expense.category, expense.description, expense.employee_id))
        connection.commit()
        if cursor.rowcount != 0:
            returned_id = cursor.fetchone()[0]
            expense.employee_id = returned_id
            return expense
        else:
            raise BadInput("Invalid information entered")

    def delete_expense_report_by_id(self, expense_id: int) -> bool:
        sql = "delete from expenses where expense_id = %s"
        cursor = connection.cursor()
        cursor.exceute(sql, [expense_id])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            raise BadInput("Invalid information entered")

    def get_total_expenses_by_id(self, employee_id: int) -> float:
        pass