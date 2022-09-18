import { useNavigate } from "react-router-dom";

const Home = () =>{

    const navigate = useNavigate();


    let joinRoomAff = async() =>{
        let response = await fetch('http://127.0.0.1:8000/api/join',{
          method: "PUT",
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({"side" : "aff"})
          
        })
        let data = await response.json()
        console.log(data)
        navigate("rooms/" + data + "/aff") 
    }
    let joinRoomNeg = async() =>{
        let response = await fetch('http://127.0.0.1:8000/api/join',{
            method: "PUT",
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({"side" : "neg"})
        })
        let data = await response.json()
        console.log(data)
        navigate("rooms/" + data + "/neg")
        
    }
    

    return (
        <div className="App">
            <div className="homePanel">
                <div className = "prompt">
                    <h1>pineapple belongs on pizza</h1>
                </div>
                <div className="buttons">
                    <button id = "agree" onClick={joinRoomAff}>agree</button>
                    <button id = "disagree" onClick={joinRoomNeg}>disagree</button>
                </div>
                
            
            </div>


        </div>
    );
}

export default Home;