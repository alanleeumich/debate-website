
const CreateUser = () =>{
   
    const api = "http://127.0.0.1:8000"

    let sendUser = async() =>{
        let username = document.getElementById("username").value
        let email = document.getElementById("email").value
        let password = document.getElementById("password").value

        let response = await fetch(api + '/api/create-user',{
            method: "PUT",
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({"username" : username,"email" : email,"password" : password})
            
          })
        let data = await response.json()
        console.log(data)
    }
   
    return(
        <div>
            <h1>create user</h1>
            username:
            <input id = "username"  autocomplete="off" ></input>
            email:
            <input id = "email"  autocomplete="off" ></input>
            password:
            <input id = "password"  autocomplete="off"></input>
            <button onClick = {sendUser}>SUBMIT</button>
        </div>


    );
}

export default CreateUser;