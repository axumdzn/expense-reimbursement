Feature: Employees should be able to delete an expense report
	Scenario: As an employee, I can cancel my reimbursement request so that I can fix a mistake or unneeded report
		Given I have logged in
		Given I am on the expense report page after login in
		When I click the button to delete the report
		Then That report gets deleted from the database and a successful message appears