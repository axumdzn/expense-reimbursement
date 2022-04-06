from behave import given, when, then


@given(u'I am on the expense report page after login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the expense report page after login')


@when(u'I click the button to see total expense')
def step_impl(context):
    context.expense_home.total_button().click()


@then(u'I can see the total amount of money I have requested')
def step_impl(context):
    assert context.expense_home.total_expense.value != ""

