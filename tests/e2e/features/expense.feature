Feature: Employees should be able to fill out an expense report
	Scenario: As an employee I would like to be reimbursed for type of expense
		Given I have logged in
		When I enter the correct amount
		When I enter the correct category
		When I enter a description
		When I click the submit button
		Then I get an alert saying its successful