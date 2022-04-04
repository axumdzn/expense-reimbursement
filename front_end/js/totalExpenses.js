
const employeeidInput = document.getElementById();

async function getTotal(){
    const response = await fetch(
        `http://localhost:5000/${employeeidInput.value}`,
        {
            method: "GET"
        }
    )
    if(response.status == 200){
        amount = await response.json()
        alert(amount);
    }else {
        alert("Please enter correct employee ID");
    }
}