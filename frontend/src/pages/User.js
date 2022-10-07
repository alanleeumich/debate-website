import { useParams } from 'react-router-dom'
import UserProfile from '../components/UserProfile';
const User = () =>{
   
    const api = "http://127.0.0.1:8000"
    const {username} = useParams()

    console.log(UserProfile.getUsername())
    console.log(UserProfile.getPassword())

    let getUser = async() =>{
       

        let response = await fetch(api + '/api/get-user',{
            method: "POST",
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                {"auth":
                    {
                        "username": UserProfile.getUsername(),
                        "password": UserProfile.getPassword()
                    },
                }),
            credentials: 'include'
            
          })
        let data = await response.json()
        console.log(data)
    }
    getUser()

    return(
        <div>
            {username}
        </div>


    );
}

export default User;