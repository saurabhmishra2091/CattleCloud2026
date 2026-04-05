// Importing React and useState hook for managing component state
import React, { useState } from "react";

// Importing useNavigate hook to programmatically navigate between pages
import { useNavigate } from "react-router-dom";
import Profile from "./Profile";

export default function Topbar({ setOpen }) {

  // Hook used for page navigation (for logout redirect)
  const navigate = useNavigate();

  // State to track whether dark mode is enabled or not
  const [dark, setDark] = useState(false);

  // ✅ ADDED profile picture state
  const [profilePic, setProfilePic] = useState(
    localStorage.getItem("profilePic") || ""
  );

  // ✅ ADDED image upload function
  const handleImageChange = (e) => {
    const file = e.target.files[0];

    if (file) {
      const reader = new FileReader();

      reader.onloadend = () => {
        setProfilePic(reader.result);
        localStorage.setItem("profilePic", reader.result);
      };

      reader.readAsDataURL(file);
    }
  };

  // Function executed when the Logout button is clicked
  const logout = () => {

    // Removing stored authentication data from localStorage
    localStorage.removeItem("auth");
    localStorage.removeItem("role");
    localStorage.removeItem("user");

    // Redirect user to login page
    navigate("/login");
  };

  // Function to toggle between light and dark theme
  const toggleTheme = () => {

    // Toggle the "dark" class on the body element
    document.body.classList.toggle("dark");

    // Update the dark mode state
    setDark(!dark);
  };

  return (

   // Topbar container
   <header className="topbar-fixed">

  {/* Menu button (three lines icon) used to open sidebar */}
  <button
    className="menu-btn"
    onMouseEnter={() => setOpen && setOpen(true)} // Opens sidebar when mouse enters
  >
    ☰
  </button>

  {/* Right section of the topbar */}
  <div className="topbar-right">

    {/* Theme toggle button (Moon for dark mode, Sun for light mode) */}
    <button className="icon-btn" onClick={toggleTheme}>
      {dark ? "☀️" : "🌙"}
    </button>

    {/* Display logged-in user's name from localStorage */}
    <span className="user">{localStorage.getItem("user") || "Farmer"}</span>
    {/* Profile icon */}
    <Profile logout={logout} />

  </div>

</header>
  );
}