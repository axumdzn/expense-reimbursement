const deleteBtn = document.getElementById("deletePrevious")


async function deletePrevious() {
    const previous = JSON.parse(localStorage.getItem("lastExpense"))
    const response = await fetch(`http://127.0.0.1:5000/api/expense/${previous}`,{
        method:"DELETE"
    })
    if(response.status == 200){
        const data = await response.json()
        if(data.result === true){
            alert("Previous report has successfully been removed")
        }
        else{
            alert("Delete was not successful")
        }
    }
    else{
        alert(response.statusText)
    }
}