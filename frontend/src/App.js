import './App.css';

import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CommunityHome from "./pages/CommunityHome";
import Room from "./pages/Room";
import CreateUser from "./pages/CreateUser"
import Login from "./pages/Login"
import User from "./pages/User"



function App() {
  return(
    <BrowserRouter>
      <Routes>
        <Route path = "/rooms/:roomName/:side" element = {<Room />}/>
        <Route path = "/create-user" element = {<CreateUser/>}/>
        <Route path = "/login" element = {<Login/>}/>
        <Route path = "/user/:username" element = {<User/>}/>
        <Route exact path="/:community" element={<CommunityHome />}/>
         
      </Routes>
    </BrowserRouter>
  )
}

export default App;
