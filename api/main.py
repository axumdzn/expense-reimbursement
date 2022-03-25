from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/employee", methods=["GET"])
def employee_login():
    pass


@app.route("/api/expense", methods=["POST"])
def create_expense():
    pass


@app.route("/api/expense/<expense_id>", methods=["DELETE"])
def delete_expense_by_id():
    pass


@app.route("/api/expense/<expense_id>", methods=["GET"])
def get_total_expenses_by_id():
    pass


app.run()
