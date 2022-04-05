
const employeeidInput = document.getElementById();
const totalh1 = document.getElementById("totalExpense");

async function getTotal(){
    const response = await fetch(
        `http://localhost:5000/${employeeidInput.value}`, 
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