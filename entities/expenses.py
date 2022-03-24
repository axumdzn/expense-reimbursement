class Expense:

    def __init__(self, expense_id: int, amount: float, category: str, description: str, employee_id: int):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description
        self.employee_id = employee_id
        