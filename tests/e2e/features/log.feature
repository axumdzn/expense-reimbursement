Feature: Employees should be able to log in and log out
	Scenario: as an Employee I want to log in to my account so I can fill out my expense report
		Given I am on the login page
		When I enter my username
		When I enter my password
		When I click the login button
		Then I should be logged in and redirected to the employee expense report page
	Scenario:As an Employee I want to log out to ensure no one else uses my account
		Given I am logged in
		When I click the logout button at the bottom of the menu
		Then I should be logged out and redirected to the login page


