const amountInp = document.getElementById("amount")
const categoryInp = document.getElementById("category")
const descriptionInp = document.getElementById("description")
const expenseBtn = document.getElementById("createbtn")

let url
async function createExpense() {
    const employee = localStorage.getItem("employee");
    // in here should be an if statement that checks that category is something that has been decided as acceptable. these category hasnt been chosen yet therefore i is not implemented
    if(categoryInp.value != "travel" | ""){
        return alert("This category does not exist")
    }
    const information = {
        amount: amountInp.value,
        category: categoryInp.value,
        description: descriptionInp.value,
        employeeId: employee.employeeId,
    };
    let config = {
        method:"POST",
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify(information)
    };
    const response = await fetch(url,config)
    if(response.status === 200){
        alert("Expense has been successfully sent")
        // this is where we would have ot add to the total expense 
        // I am personally not sure if i just want to call the total expense function to do it or to manually add it the total to it now therefore i will wait to implement this till the other functions become complete
    } else{
        alert("Expense was not sent please try again")
    }
}