import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="nav-logo">
        🐮 CattleCloud
      </div>

      <nav className="nav-actions">
        <a href="#features">Features</a>
        <a href="#how">How It Works</a>
        <a href="#contact">Contact</a>

        <Link to="/login" className="btn-outline">
          Login
        </Link>

        <Link to="/register" className="btn-primary">
          Register
        </Link>
      </nav>
    </header>
  );
}