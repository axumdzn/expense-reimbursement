from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class ExpenseHome:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username(self):
        element: WebElement = self.driver.find_element(By.ID, "username")
        return element

    def password(self):
        element: WebElement = self.driver.find_element(By.ID, "password")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "log")
        return element

    def logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logout")
        return element

    def amount(self):
        element: WebElement = self.driver.find_element(By.ID, "amount")
        return element

    def category(self):
        element: WebElement = self.driver.find_element(By.ID, "category")
        return element

    def description(self):
        element: WebElement = self.driver.find_element(By.ID, "description")
        return element

    def expense_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createbtn")
        return element

    def delete_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deletePrevious")
        return element

    def total_button(self):
        element: WebElement = self.driver.find_element(By.ID, "total")
        return element

    def total_expense(self):
        element: WebElement = self.driver.find_element(By.ID, "totalExpense")
        return element
