# Test Plan
## Technologies Used
### Languages: 
 - PostgresSQL
 - Python
 - HTML
 - CSS
 - JS
 
### IDE/Other: 
 - PyCharm
 - DBeaver
 - Postman
 - GitHub
 - AWS Database
 - EC2 system
 - VSCode
### Packages: 
 - Flask
 - Flask-cors
 - Psycopg[Binary]
 - PyTest 
 - Behave
 - Selenium


## Deadlines
### Timeline: 3 Weeks
	[1-3] Writing the documentation for the project
	[4] Each person is writing tests for their assigned area
	[5-6]Writing and making sure that each work passes their tests
	[7-8] Writing/Running API Layer and the tests that come with
	[9-10]  Fixing Bugs that still occur in the back end and start to implement the front end
	[11-12] Front-end functions and making frant and back end work with each other
    [13] Features writted and tested to make sure they work
    [14] Styling/ Fixing all of the last minute things that could possible go wrong
    [15] Presentation
### Due Date: April 8, 2022

## What is Being Tested

 ### Test Suite - Employee Data(DAO) (Grace)
 - Test to make sure that employee ID is valid
 - Test to make sure employees first name and last name may not exceed 20 characters
 - Test to make sure that employee has unique Id


### Test Suite - Expense Data(DAO) (Julio)

 - Test that reimbursement requests are in numeric form
 - Test that reimbursement requests are between $1 and $1000
 - Test that employees can see the total amount of money they have requested
 - Test that reimbursement request comments are in non numeric (string) form


### Test Suite - Employee Service (Kenneth)
 - Test that each employees information is using the correct type
 - Test that employees can change their information when needed
 - Test that an employee can be deleted from the system when they are no longer needed
 - Test that can get info of an employee information when asked for it.
 - Test to make sure that all information is filled and not null when the message is called

### Test Suite - Expense Service (Joseph)
 - Test below will include positive and negative inputs by Employee: 
 - Test that Employee reimbursement entered are between $1 and $1000
 - Test that Employee reimbursement request comments must be no longer than 100 characters
 - Test that Employee reimbursement requests must be in numeric form
 - Test that Employee chooses an associated category for reimbursement 
 - Test that Employee should be able to cancel reimbursement request

## Entities
```
Create table Employees(
	employee_id: serial primary key,
	first_name varchar(20),
	last_name varchar(20),
	username varchar(20),
	password varchar(20)
	);

 Create table Expense(
	expense_id: serial primary key,
	amount dec(5,2),
	category varchar(20),
	description varchar(100),
	employee_id int,
	CONSTRAINT employee_fk FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
);
```
## User Stories
 - As an employee, I can create a login so that I can log reimburse expenses (employee_login) 
 - As an employee, I can fill out/create an expense reimbursement form so that I can get reimbursement (create_expense)  
 - As an employee, I can cancel my reimbursement request so that I can fix a mistake or unneeded report (delete_expense_by_id) 
 - As an employee, I can see the total amount of money I have requested so that I can see how much I have reported(get_total_expenses_by_id) 
 - As an employee, I wanted to logout because I am done with adding all the expenses. So that I can submit for review(employee_logout) 
## Acceptance Criteria
### Feature: Employees should be able to log in and log out
 - Scenario: as an Employee I want to log in to my account so I can fill out my expense report
	- Given I am on the login page
	- When I enter my username
	- When I enter my password
	- When I click the login button
	- Then I should be logged in and redirected to the employee expense report page
 - Scenario:As an Employee I want to log out to ensure no one else uses my account
	- Given I am logged in
	- When I click the logout button at the bottom of the menu
	- Then I should be logged out and redirected to the login page
### Feature: Employees should be able to fill out an expense report
- Scenario: As an employee I would like to be reimbursed for type of expense
	- Given I have logged in
	- When I enter the correct amount
	- When I enter the correct category
	- When I enter a description
	- When I click the submit button
	- Then I get an alert saying its successful

### Feature: Employees should be able to view a monetary summary of previous expense reports
- Scenario: As an employee, I can see the total amount of money I have requested
	- Given I have logged in
	- When I click the button to see total expense
	- Then  I can see the total amount of money I have requested

### Feature: Employees should be able to delete an expense report
- Scenario: As an employee, I can cancel my reimbursement request so that I can fix a mistake or unneeded report
	- Given I am logged in
	- Given I have created an expense
	- When I click the button to delete the report
	- Then That report gets deleted from the database and a successful message appears