
const totalh1 = document.getElementById("totalExpense");
// all functions need the correct routes in order to function
async function getTotal(){
    const employeeInfo = JSON.parse(localStorage.getItem('employee'))
    console.log(employeeInfo.employeeId);
    const response = await fetch(
        `http://127.0.0.1:5000/api/expense/${employeeInfo["employeeId"]}`, 
        {
            method: "GET"
        }
    )
    if(response.status == 200){
        amount = await response.json()
        totalh1.textContent = `$${amount.amount}`
    }else {
        alert("Please enter correct employee ID");
    }
}

getTotal()