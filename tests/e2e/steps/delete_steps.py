from behave import given, when, then


@given(u'I have logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have logged in')


@given(u'I am on the expense report page after login in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the expense report page after login in')


@when(u'I click the button to delete the report')
def step_impl(context):
    context.expense_home.delete_button().click()



@then(u'That report gets deleted from the database and a successful message appears')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then That report gets deleted from the database and a successful message appears')

