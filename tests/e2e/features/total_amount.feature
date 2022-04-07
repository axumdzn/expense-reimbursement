Feature: Employees should be able to view a monetary summary of previous expense reports
	Scenario: As an employee, I can see the total amount of money I have requested
		Given I have logged in
		When I click the button to see total expense
		Then  I can see the total amount of money I have requested