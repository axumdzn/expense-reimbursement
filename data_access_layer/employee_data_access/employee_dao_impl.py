from custom_exception.bad_input import BadInput
from data_access_layer.employee_data_access.employee_dao_interface import EmployeeDAOInterface
from entities.employee import Employee
from util.manage_connection import connection


class EmployeeDAOImp(EmployeeDAOInterface):

    def dao_employee_login(self, username, password: str) -> Employee:
        sql = "select * from employees where username = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        connection.commit()
        employee = cursor.fetchone()
        employee_data = Employee(*employee)
        if employee_data.password != password:
            raise BadInput("wrong username or password: please try again")
        else:
            return employee_data





