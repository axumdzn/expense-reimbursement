from behave import given, when, then
from selenium.webdriver.support.expected_conditions import alert_is_present, title_contains
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I have logged in')
def step_impl(context):
    context.driver.get("C:/Users/kennf/code/revature/expense-reimbursement/front_end/html/index.html")
    context.expense_home.username().send_keys("jefferson")
    context.expense_home.password().send_keys("password")
    context.expense_home.login_button().click()


@given(u'I have created an expense')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(title_contains("Expense Reimbursement"))
    context.expense_home.amount().send_keys(500.00)
    context.expense_home.category().send_keys("travel")
    context.expense_home.description().send_keys("Company workshop fail")
    context.expense_home.expense_button().click()
    WebDriverWait(context.driver, 4).until(alert_is_present())
    context.expense_home.get_alert().accept()




@when(u'I click the button to delete the report')
def step_impl(context):
    context.expense_home.delete_button().click()


@then(u'That report gets deleted from the database and a successful message appears')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())
    assert context.expense_home.get_alert().text == "Previous report has successfully been removed"

