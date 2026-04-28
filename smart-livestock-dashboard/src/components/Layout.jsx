// Importing useState hook to manage sidebar open/close state
import { useState } from "react";

// ✅ Import Outlet + useNavigate
import { Outlet, useNavigate } from "react-router-dom";

// Importing layout components
import Sidebar from "./Sidebar";
import Topbar from "./Topbar";
import Footer from "./Footer";

export default function Layout({ lang, setLang }) {

  // State to control sidebar
  const [open, setOpen] = useState(false);

  // ✅ FIX: define navigate
  const navigate = useNavigate();

  const logout = () => {
    if (window.confirm("Logout from system?")) {
      localStorage.removeItem("auth");
      localStorage.removeItem("user");
      navigate("/login");
    }
  };

  return (

    <div className="app-wrapper">

      {/* Topbar */}
      <Topbar setOpen={setOpen} lang={lang} setLang={setLang} />

      {/* Sidebar */}
      <Sidebar open={open} setOpen={setOpen} lang={lang} />

      {/* Main content */}
      <main className="main-content">
        <Outlet />
      </main>

      {/* Footer */}
      <Footer lang={lang} />

    </div>
  );
}