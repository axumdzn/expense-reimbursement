from behave import given, when, then


@given(u'I have logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have logged in')


@given(u'I am on the expense report page after login in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the expense report page after login in')


@when(u'I enter the correct {amount}')
def step_impl(context, amount: float):
    context.expense_home.amount().send_keys(amount)


@when(u'I enter the correct {category}')
def step_impl(context, category: str):
    context.expense_home.category().send_keys(category)


@when(u'I enter a {description}')
def step_impl(context, description: str):
    context.expense_home.description().send_keys(description)


@when(u'I click the submit button')
def step_impl(context):
    context.expense_home.expense_button().click()


@then(u'I get an alert saying its successful')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get an alert saying its successful')

