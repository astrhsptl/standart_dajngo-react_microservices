import React, { useEffect, useState } from "react";
import Temp from "./components/temp";
import {BrowserRouter,Route, Routes} from "react-router-dom";
import LoginComponent from "./components/LoginComponent";
import RegiterComponent from "./components/RegiterComponent";

function App() {
  let [user, setUser] = useState({
    username: '',
    email: '',
    password: '',
    access: '',
    refresh: '',
  });
  useEffect(() => {
    console.log(`user: ${user.access}`)
  }, [user])
  return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Temp user={user}/>}/>  {/*Start Page*/}
          <Route path="/login" element={<LoginComponent user={user} setUser={setUser}/>}/> {/* Login Form */}
          <Route path="/register" element={<RegiterComponent user={user} setUser={setUser}/>}/> {/* Register form */}
        </Routes>
      </BrowserRouter>
  );
}

export default App;
