from flask import Flask, request

app: Flask = Flask(__name__)


@app.get("/data")
def expense_dao_sum():
    query = request.args["select sum[amount] from employee_id;"]
    if query == "":
        return expense[employee_id]
    else:
        return expense[query]


