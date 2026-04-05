// Import React hooks
import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Login() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [show,setShow]=useState(false);
  const [error, setError] = useState("");

  // ✅ UPDATED LOGIN FUNCTION (BACKEND)
  const submit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("http://localhost:5000/api/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.message || "Login failed");
        return;
      }

      // ✅ SAVE TOKEN + USER
      localStorage.setItem("token", data.token);
      localStorage.setItem("user", data.name);
      localStorage.setItem("auth", "true");

      navigate("/farmer-dashboard");

    } catch (err) {
      setError("Server error");
    }
  };

  return (
    <div className="auth-bg">

      <form className="auth-card" onSubmit={submit} style={{background:"none"}}>

        <h2 style={{fontSize:"30px",fontWeight:"lighter",textAlign:"center"}}>
          Welcome to
        </h2>

        <h2 style={{fontSize:"40px",textAlign:"center"}}>
          CattleCloud
        </h2>

        <div style={{marginLeft:"20%"}}>

          <div style={{fontWeight:"bold",color:"aquamarine"}}>
            Email:-
          </div>

          <input
            type="email"
            placeholder="Email Address"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{display:"block",fontSize:"15px",marginBottom:"10px"}}
          />

          {error && (
            <p style={{ color: "red", fontSize: "14px" }}>
              {error}
            </p>
          )}

          <div style={{fontWeight:"bold",color:"aquamarine"}}>
            Password:-
          </div>

          <div style={{position:"relative", width:"fit-content"}}>

            <input
              type={show ? "text" : "password"}
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              style={{
                display:"block",
                fontSize:"15px",
                paddingRight:"40px"
              }}
            />

            <button
              type="button"
              onClick={() => setShow(!show)}
              style={{
                position:"absolute",
                right:"5px",
                top:"50%",
                transform:"translateY(-50%)",
                background:"none",
                border:"none",
                cursor:"pointer"
              }}
            >
              {show ? "🙈" : "👁️"}
            </button>

          </div>
        </div>

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
            marginLeft:"120px"
          }}
        >
          Login
        </button>

        <div style={{color:"white",marginTop:"10px",textAlign:"center"}}>
          if you forgot your password?
          <a href={"/forgot-password"} style={{color:"aquamarine"}}>Forgot Password</a>
        </div>

        <div style={{color:"white",marginTop:"10px",textAlign:"center"}}>
          Don't have an account?
          <a href={"/register"} style={{color:"aquamarine"}}>Signup</a>
        </div>

      </form>
    </div>
  );
}