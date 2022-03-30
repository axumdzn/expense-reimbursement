

from entities.expenses import Expense
from util.manage_connection import connection
from service.expenses.expense_interface import ExpenseServiceInterface


class ExpenseServiceImp(ExpenseServiceInterface):

    def service_create_expense_report(self, expense: Expense) -> Expense:
        sql = "insert into expense report(default,%s,%s,%s,default) returning expense_id"
        cursor = connection.cursor()
        cursor.exceute(sql, (expense.amount, expense.category, expense.description))
        connection.commit()
        new_expense_id = cursor.fetchone()[0]
        expense.expanse_id = new_expense_id
        return expense

    def service_get_total_expense_by_id(self, employee_id: int) -> list[Expense]:
        sql = "select * from expenses"
        cursor = connection.cursor()
        cursor.exceute(sql)
        expense_records = cursor.fetchall()
        expense_list = []
        for employee_id in expense_records:
            employee = Expense(*employee_id)
            expense_list.append(employee)
        return sum(expense_list)

    def service_expense_delete(self, expense_id: int) -> bool:
        sql = "delete from expense where expense_id = %s"
        cursor = connection.cursor()
        cursor.exceute(sql, [expense_id])
        connection.commit()
        return True

