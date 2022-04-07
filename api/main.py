from flask import Flask, jsonify, request
from flask_cors import CORS

from dal.expense_dal.expense_dao_imp import ExpenseDAOImp
from dal.employee_data_access.employee_dao_impl import EmployeeDAOImp
from entities.employee import Employee
from entities.expenses import Expense
from service.employee_service.employee_service_imp import EmployeeServiceImp
from service.expenses.expense_imp import ExpenseServiceImp


app = Flask(__name__)
CORS(app)
employee_dao = EmployeeDAOImp()
employee_service = EmployeeServiceImp(employee_dao)
expense_dao = ExpenseDAOImp()
expense_service = ExpenseServiceImp(expense_dao)


@app.route("/api/employee", methods=["POST"])
def employee_login():
    employee_data = request.get_json()
    login_credentials = employee_service.service_employee_login(employee_data["username"], employee_data["password"])
    if login_credentials.username == employee_data["username"]:
        result = {
            "firstName": login_credentials.first_name,
            "lastName": login_credentials.last_name,
            "username": login_credentials.username,
            "password": login_credentials.password,
            "employeeId": login_credentials.employee_id
        }
        return jsonify(result), 200
    else:
        return jsonify(login_credentials), 400


@app.route("/api/expense", methods=["POST"])
def create_expense():
    data: dict = request.get_json()
    expense = Expense(data["expenseId"], float(data["amount"]), data["category"], data["description"], data["employeeId"])
    global expense_service
    result = expense_service.service_create_expense_report(expense)
    if result.amount == float(data["amount"]):
        data["expenseId"] = result.expense_id
        return jsonify(data), 200
    else:
        return jsonify(result), 400


@app.route("/api/expense/<expense_id>", methods=["DELETE"])
def delete_expense_by_id(expense_id: str):
    expense_id = int(expense_id)
    result = expense_service.service_expense_delete(expense_id)
    result_dictionary = {"result": result}
    result_json = jsonify(result_dictionary)
    return result_json, 200


@app.route("/api/expense/<employee_id>", methods=["GET"])
def get_total_expenses_by_id(employee_id: str):
    employee_data = int(employee_id)
    global expense_service
    result = expense_service.service_get_total_expense_by_id(employee_data)
    if type(result) is float:
        return jsonify({"amount": result}), 200
    else:
        return jsonify(result), 400


app.run()
