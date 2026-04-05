// Importing React and useState hook to manage component state
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Register() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [error, setError] = useState("");

  const submit = async (e) => {
    e.preventDefault();

    if(phone.length !== 10){
      setError("Enter valid phone number");
      return;
    }

    if (!email.endsWith("@gmail.com")) {
      setError("Only Gmail accounts are allowed.");
      return;
    }

    const name = document.querySelector('input[placeholder="Farmer Name"]').value;
    const password = document.querySelector('input[placeholder="Password"]').value;

    try {
      const res = await fetch("http://localhost:5000/api/auth/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name,
          email,
          password
        })
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.message || "Registration failed");
        return;
      }

      alert("Registration Successful");

      navigate("/login");

    } catch (err) {
      setError("Server error");
    }
  };

  return (

    <div className="auth-bg">

      <form className="auth-card" onSubmit={submit} style={{background:"none"}}>

        <h2 style={{textAlign:"center",fontSize:"30px"}}>Farmer Registration</h2>

        <div style={{margin:"20%"}}>

          <div style={{fontWeight:"bold"}}>Farmer Name:-</div>
          <input placeholder="Farmer Name" required style={{fontSize:"15px"}}/>

          <div style={{fontWeight:"bold",marginTop:"10px"}}>Farmer Address:-</div>
          <input placeholder="Farmer Address" required style={{fontSize:"15px"}}/>

          <div style={{fontWeight:"bold",marginTop:"10px"}}>Mobile No.:-</div>
          <input
            placeholder="Mobile No."
            required
            style={{fontSize:"15px"}}
            value={phone}
            onChange={(e)=>setPhone(e.target.value)}
          />

          <div style={{fontWeight:"bold",marginTop:"10px"}}>Email ID:-</div>
          <input
            placeholder="Email ID"
            required
            style={{fontSize:"15px"}}
            value={email}
            onChange={(e)=>setEmail(e.target.value)}
          />

          {error && (
            <p style={{color:"red",fontSize:"14px"}}>
              {error}
            </p>
          )}

          <div style={{fontWeight:"bold",marginTop:"10px"}}>Password:-</div>
          <input placeholder="Password" required style={{fontSize:"15px"}}/>

          <button
            type="submit"
            style={{
              color:"white",
              backgroundColor:"aqua",
              padding:"10px",
              width:"fit-content",
              fontSize:"20px",
              textAlign:"center",
              borderRadius:"25px",
              margin:"10px",
              marginLeft:"20%"
            }}
          >
            Register
          </button>

          <div style={{color:"white",marginTop:"10px",textAlign:"center"}}>
            Already have an Account?
            <a href={"/login"} style={{color:"aquamarine"}}>Login</a>
          </div>

        </div>

      </form>

    </div>
  );
}