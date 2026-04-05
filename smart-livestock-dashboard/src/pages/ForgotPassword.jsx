import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function ForgotPassword() {

const navigate = useNavigate();

const [email, setEmail] = useState("");
const [code, setCode] = useState("");
const [newPassword, setNewPassword] = useState("");
const [generatedCode, setGeneratedCode] = useState(null);
const [step, setStep] = useState(1);
const [message, setMessage] = useState("");
const [error, setError] = useState("");

// STEP 1: CHECK EMAIL AND GENERATE CODE
const handleSubmit = (e) => {
  e.preventDefault();

  const storedUsers = localStorage.getItem("users");

  const users = storedUsers ? JSON.parse(storedUsers) : [];

  console.log("Users:", users);
  console.log("Entered Email:", email);

  const user = users.find(
    (u) => (u.email || "").toLowerCase() === email.toLowerCase()
  );

  if (!user) {
    setError("Email not found");
    return;
  }

  setError("");

  const randomCode = Math.floor(100000 + Math.random() * 900000);

  setGeneratedCode(randomCode);

  setMessage("Verification Code: " + randomCode);

  setStep(2);
};

// STEP 2: VERIFY CODE
const verifyCode = (e) => {
e.preventDefault();


if (parseInt(code) === generatedCode) {
  setMessage("Code verified successfully");
  setStep(3);
} else {
  setMessage("Invalid verification code");
}


};

// STEP 3: UPDATE PASSWORD
const updatePassword = (e) => {
e.preventDefault();


const users = JSON.parse(localStorage.getItem("users") || "[]");

const updatedUsers = users.map((user) => {
  if (user.email?.toLowerCase() === email.toLowerCase()) {
    return { ...user, password: newPassword };
  }
  return user;
});

localStorage.setItem("users", JSON.stringify(updatedUsers));

setMessage("Password updated successfully");

setTimeout(() => {
  navigate("/login");
}, 2000);


};

return ( <div className="auth-bg">
<div className="auth-card" style={{ background: "none" }}>

```
    <h2 style={{ fontSize: "40px", textAlign: "center" }}>
      Forgot Password
    </h2>

    {/* STEP 1 EMAIL */}
    {step === 1 && (
      <form
        onSubmit={handleSubmit}
        style={{ display: "flex", gap: "10px", alignItems: "center" }}
      >
        <div style={{ marginLeft: "20%" }}>
          <div style={{ fontWeight: "bold", color: "aquamarine" }}>
            Email:-
          </div>

          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{
              display: "block",
              fontSize: "15px",
              marginBottom: "10px",
            }}
          />

          {error && (
            <p style={{ color: "red", fontSize: "14px" }}>{error}</p>
          )}
        </div>

        <button type="submit" 
        style={{
            background:"#27ae60",
            color:"white",
            border:"none",
            padding:"8px 20px",
            borderRadius:"8px",
            cursor:"pointer"
          }}>Send Reset Code</button>
      </form>
    )}

    {/* STEP 2 VERIFY CODE */}
    {step === 2 && (
      <form
        onSubmit={verifyCode}
        style={{ display: "flex", gap: "10px", alignItems: "center" }}
      >
        <div style={{ marginLeft: "20%" }}>
          <div style={{ fontWeight: "bold", color: "aquamarine" }}>
            Verification Code:-
          </div>

          <input
            type="text"
            placeholder="Enter code"
            value={code}
            onChange={(e) => setCode(e.target.value)}
            required
            style={{
              display: "block",
              fontSize: "15px",
              marginBottom: "10px",
            }}
          />
        </div>

        <button type="submit"
        style={{
            background:"#27ae60",
            color:"white",
            border:"none",
            padding:"8px 20px",
            borderRadius:"8px",
            cursor:"pointer"
          }}>Verify</button>
      </form>
    )}

    {/* STEP 3 NEW PASSWORD */}
    {step === 3 && (
      <form
        onSubmit={updatePassword}
        style={{ display: "flex", gap: "10px", alignItems: "center" }}
      >
        <div style={{ marginLeft: "20%" }}>
          <div style={{ fontWeight: "bold", color: "aquamarine" }}>
            New Password:-
          </div>

          <input
            type="password"
            placeholder="Enter new password"
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
            required
            style={{
              display: "block",
              fontSize: "15px",
              marginBottom: "10px",
            }}
          />
        </div>

        <button type="submit"
        style={{
            background:"#27ae60",
            color:"white",
            border:"none",
            padding:"8px 20px",
            borderRadius:"8px",
            cursor:"pointer"
          }}>Update Password</button>
      </form>
    )}

    {/* MESSAGE */}
    {message && (
      <p style={{ textAlign: "center", marginTop: "10px", color: "red" }}>
        {message}
      </p>
    )}

    {/* BACK TO LOGIN */}
    <div style={{ color: "white", marginTop: "10px", textAlign: "center" }}>
      Want to go to Login Page?
      <a href={"/login"} style={{ marginLeft: "10px" }}>
        login
      </a>
    </div>

  </div>
</div>

);
}