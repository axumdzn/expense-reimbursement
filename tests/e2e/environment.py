from selenium import webdriver
from behave.runner import Context

from pom.index_pom import ExpenseHome


def before_all(context: Context):
    context.driver = webdriver.Chrome("tests/e2e/chromedriver.exe")
    context.expense_home = ExpenseHome(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
