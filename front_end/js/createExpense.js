const amountInp = document.getElementById("amount")
const categoryInp = document.getElementById("category")
const descriptionInp = document.getElementById("description")
const expenseBtn = document.getElementById("createbtn")
// all this needs is correct url
let url = "http://127.0.0.1:5000/api/expense"
async function createExpense() {
    const employee = JSON.parse(localStorage.getItem("employee"));
    if(categoryInp.value != "travel" | "food" | "office" | "equipment" | "other"){
        return alert("This category does not exist")
    }
    const information = {
        expenseId: 0,
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
        let data = await response.json()
        localStorage.setItem("lastExpense", data.expenseId)
        alert("Expense has been successfully sent")
        amountInp.value =""
        categoryInp.value =""
        descriptionInp.value =""

    } else{
        alert("Expense was not sent please try again")
    }
}