from custom_exception.bad_input import BadInput
from dal.employee_data_access.employee_dao_interface import EmployeeDAOInterface
from entities.employee import Employee
from util.manage_connection import connection


class EmployeeDAOImp(EmployeeDAOInterface):

    def dao_employee_login(self, username, password: str) -> Employee:
        sql = "select * from employees where username = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        connection.commit()
        employee = cursor.fetchone()
        if cursor.rowcount == 0:
            raise BadInput("wrong username or password")
        employee_data = Employee(*employee)
        if employee_data.password != password:
            raise BadInput("wrong username or password")
        else:
            return employee_data





