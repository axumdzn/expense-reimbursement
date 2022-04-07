from behave.runner import Context
from selenium import webdriver

from pom.index_pom import ExpenseHome


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.expense_home = ExpenseHome(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
