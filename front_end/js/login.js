const usernameInput = document.getElementById("username")
const passwordInput = document.getElementById('password')



async function sendMessage(){
   
    
    let loginCredentials ={username: usernameInput.value, password: passwordInput.value}
    let config = {
        method: "POST",
        headers: {'Content-Type' : "application/json"},
        body: JSON.stringify(loginCredentials)
        }

        const response = await fetch ("username",config)

        
    if(response.status === 200) {

        username = await response.json();
        window.localStorage.setItem("username", username);
        
        window.location.href = "expense.html"
          
        
    }else {

        alert("Please enter correct login credentials");

        
    }



}










