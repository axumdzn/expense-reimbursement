from behave import given, when, then

#
# @given(u'I have logged in')
# def step_impl(context):
#     context.driver.get("C:/Users/kennf/code/revature/expense-reimbursement/front_end/html/index.html")
#     context.expense_home.username().send_keys("jefferson")
#     context.expense_home.password().send_keys("password")
#     context.expense_home.login_button().click()
#
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait


@when(u'I enter the correct amount')
def step_impl(context):
    context.expense_home.amount().send_keys(500.00)


@when(u'I enter the correct category')
def step_impl(context):
    context.expense_home.category().send_keys("travel")


@when(u'I enter a description')
def step_impl(context):
    context.expense_home.description().send_keys("Company workshop")


@when(u'I click the submit button')
def step_impl(context):
    context.expense_home.expense_button().click()


@then(u'I get an alert saying its successful')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())
    assert context.expense_home.get_alert().text == "Expense has been successfully sent"

