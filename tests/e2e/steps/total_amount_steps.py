from behave import given, when, then

#
# @given(u'I have logged in')
# def step_impl(context):
#     context.driver.get("C:/Users/kennf/code/revature/expense-reimbursement/front_end/html/index.html")
#     context.expense_home.username().send_keys("jefferson")
#     context.expense_home.password().send_keys("password")
#     context.expense_home.login_button().click()
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait


@when(u'I click the button to see total expense')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(title_contains("Expense Reimbursement"))
    context.expense_home.total_button().click()


@then(u'I can see the total amount of money I have requested')
def step_impl(context):
    assert context.expense_home.total_expense().text != ""

