// Importing NavLink component from react-router-dom
import { NavLink } from "react-router-dom";

// ✅ Import translations
import { text } from "../utils/translations";

export default function Sidebar({ open, setOpen, lang }) {

  // ✅ SAFE FALLBACK
  const t = text[lang] || text["en"];

  return (
    // Sidebar navigation container
    <nav
      className="horizontal-nav"

      onMouseEnter={() => setOpen(true)}
      onMouseLeave={() => setOpen(false)}

      style={{
        display: open ? "flex" : "none",
        flexDirection: "column",
        position: "absolute",
        top: "50px",
        left: "10px",
        background: "lightgreen",
        border: "1px solid #ccc",
        padding: "10px",
        zIndex: 1000,
      }}
    >

      {/* Navigation link to Farmer Dashboard */}
      <NavLink to="/farmer-dashboard" style={{color:"black", padding:"5px"}}>
        {t.dashboard}
      </NavLink>

      {/* Navigation link to Animals page */}
      <NavLink to="/animals" style={{color:"black", padding:"5px"}}>
        {t.animals}
      </NavLink>

      {/* Navigation link to Milk page */}
      <NavLink to="/milk" style={{color:"black", padding:"5px"}}>
        {t.milk}
      </NavLink>

      {/* Navigation link to Vaccination page */}
      <NavLink to="/vaccination" style={{color:"black", padding:"5px"}}>
        {t.vaccination}
      </NavLink>

      {/* Navigation link to Expenses page */}
      <NavLink to="/expenses" style={{color:"black", padding:"5px"}}>
        {t.expenses}
      </NavLink>

    </nav>
  );
}