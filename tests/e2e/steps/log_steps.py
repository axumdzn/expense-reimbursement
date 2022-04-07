from behave import given, when, then
# behave /folder_path/file.feature --outfile /path_to_log/name.log
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am on the login page')
def step_impl(context):
    context.driver.get("C:/Users/kennf/code/revature/expense-reimbursement/front_end/html/index.html")


@when(u'I enter my username')
def step_impl(context):
    context.expense_home.username().send_keys("jefferson")


@when(u'I enter my password')
def step_impl(context):
    context.expense_home.password().send_keys("password")


@when(u'I click the login button')
def step_impl(context):
    context.expense_home.login_button().click()


@then(u'I should be logged in and redirected to the employee expense report page')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(title_contains("Expense Reimbursement"))
    assert context.driver.title == "Expense Reimbursement"


# need to ask eric about this/ do you need to do this if you are already logged in
@given(u'I am logged in')
def step_impl(context):
    context.driver.get("C:/Users/kennf/code/revature/expense-reimbursement/front_end/html/index.html")
    context.expense_home.username().send_keys("jefferson")
    context.expense_home.password().send_keys("password")
    context.expense_home.login_button().click()


@when(u'I click the logout button at the bottom of the menu')
def step_impl(context):
    context.expense_home.logout_button().click()


@then(u'I should be logged out and redirected to the login page')
def step_impl(context):
    assert context.driver.title == "Expense Login"

