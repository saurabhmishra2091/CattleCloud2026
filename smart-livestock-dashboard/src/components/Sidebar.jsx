// Importing NavLink component from react-router-dom
// NavLink is used for navigation between pages and highlights the active route
import { NavLink } from "react-router-dom";

export default function Sidebar({ open, setOpen }) {
  return (
    // Sidebar navigation container
    <nav
      className="horizontal-nav"

      // Opens the sidebar when the mouse enters the sidebar area
      onMouseEnter={() => setOpen(true)}

      // Closes the sidebar when the mouse leaves the sidebar area
      onMouseLeave={() => setOpen(false)}

      style={{
        // Show sidebar only when "open" state is true
        display: open ? "flex" : "none",

        // Arrange navigation links vertically
        flexDirection: "column",

        // Position the sidebar relative to the top-left of the page
        position: "absolute",
        top: "50px",
        left: "10px",

        // Background color of the sidebar
        background: "lightgreen",

        // Border around the sidebar
        border: "1px solid #ccc",

        // Padding inside the sidebar
        padding: "10px",

        // Keeps sidebar above other elements
        zIndex: 1000,
      }}
    >

      {/* Navigation link to Farmer Dashboard */}
      <NavLink to="/farmer-dashboard" style={{color:"black", padding:"5px"}}>
        Dashboard
      </NavLink>

      {/* Navigation link to Animals page */}
      <NavLink to="/animals" style={{color:"black", padding:"5px"}}>
        Animals
      </NavLink>

      {/* Navigation link to Milk page */}
      <NavLink to="/milk" style={{color:"black", padding:"5px"}}>
        Milk
      </NavLink>

      {/* Navigation link to Vaccination page */}
      <NavLink to="/vaccination" style={{color:"black", padding:"5px"}}>
        Vaccination
      </NavLink>

      {/* Navigation link to Expenses page */}
      <NavLink to="/expenses" style={{color:"black", padding:"5px"}}>
        Expenses
      </NavLink>

    </nav>
  );
}