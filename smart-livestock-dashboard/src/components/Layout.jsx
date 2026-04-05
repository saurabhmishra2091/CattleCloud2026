// Importing useState hook to manage sidebar open/close state
import { useState } from "react";

// Importing Outlet from react-router-dom to render child routes
import { Outlet } from "react-router-dom";

// Importing layout components
import Sidebar from "./Sidebar";  // Sidebar navigation component
import Topbar from "./Topbar";    // Topbar component (menu, theme toggle, logout)
import Footer from "./Footer";    // Footer component

export default function Layout() {

  // State to control whether the sidebar is open or closed
  const [open, setOpen] = useState(false);

  const logout=()=>{

 if(window.confirm("Logout from system?")){

  localStorage.removeItem("auth");
  localStorage.removeItem("user");

  navigate("/login");

 }

}
  return (

    // Main wrapper for the entire application layout
    <div className="app-wrapper">

      {/* Top navigation bar */}
      {/* setOpen is passed to allow Topbar to open the sidebar */}
      <Topbar setOpen={setOpen} />

      {/* Sidebar navigation */}
      {/* open controls visibility and setOpen allows sidebar to close/open */}
      <Sidebar open={open} setOpen={setOpen} />

      {/* Main content area where page components will be rendered */}
      <main className="main-content">
        {/* Outlet renders the matched route component */}
        <Outlet />
      </main>

      {/* Footer section displayed at the bottom of the page */}
      <Footer />

    </div>
  );
}