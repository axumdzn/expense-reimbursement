from flask import Flask, jsonify, request

from dal.expense_dal.expense_dao_imp import ExpenseDAOImp
from data_access_layer.employee_data_access.employee_dao_impl import EmployeeDAOImp
from service.employee_service.employee_service_imp import EmployeeServiceImp

app = Flask(__name__)
employee_dao = EmployeeDAOImp()
employee_service = EmployeeServiceImp(employee_dao)
expense_dao = ExpenseDAOImp()
expense_service = ExpenseServiceImp(expense_dao)

@app.route("/api/employee", methods=["GET"])
def employee_login():
    pass


# this is mine to write
@app.route("/api/expense", methods=["POST"])
def create_expense():
    data : dict = request.get_json()


@app.route("/api/expense/<expense_id>", methods=["DELETE"])
def delete_expense_by_id():
    pass


@app.route("/api/expense/<expense_id>", methods=["GET"])
def get_total_expenses_by_id():
    pass


app.run()
