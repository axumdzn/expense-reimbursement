from custom_exception.bad_input import BadInput
from dal.expense_dal.expense_dao_interface import ExpenseDAOInterface
from entities.employee import Employee
from entities.expenses import Expense
from util.manage_connection import connection


class ExpenseDAOImp(ExpenseDAOInterface):

    def create_expense_report(self, expense: Expense) -> Expense:
        sql = "insert into expenses values(default, %s, %s, %s, %s) returning expense_id"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (expense.amount, expense.category, expense.description, expense.employee_id))
        connection.commit()
        if cursor.rowcount != 0:
            returned_id = cursor.fetchone()[0]
            expense.expense_id = returned_id
            return expense
        else:
            raise BadInput("Invalid information entered")

    def delete_expense_report_by_id(self, expense_id: int) -> bool:
        sql = "delete from expenses where expense_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [expense_id])

        connection.commit()
        print(cursor.rowcount)
        if cursor.rowcount != 0:
            return True
        else:
            raise BadInput("Invalid information entered")

    def get_total_expenses_by_id(self, employee_id: int) -> float:
        sql = "select sum(amount) from expenses where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        result = cursor.fetchone()[0]
        if result is not None:
            return result
        else:
            raise BadInput("This user does not exist")
