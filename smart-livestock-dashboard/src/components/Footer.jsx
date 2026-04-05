import React from "react";

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container" 
      style={{height:"fit-content"}}>

        <div className="footer-section">
          <h3>Services</h3>
          <ul>
            <a href="http://localhost:5173/animals" style={{display:"block",color:"lightblue",textDecoration:"none"}}>Animal Health Tracking</a>
            <a href="http://localhost:5173/vaccination" style={{display:"block",color:"lightblue",textDecoration:"none"}}>Breed Management</a>
            <a href="http://localhost:5173/milk" style={{display:"block",color:"lightblue",textDecoration:"none"}}>Milk Production</a>
            <a href="http://localhost:5173/expenses" style={{display:"block",color:"lightblue",textDecoration:"none"}}>Farmer Support</a>
          </ul>
        </div>
        <div className="footer-section">
          <h2>CattleCloud</h2>
          <p style={{fontSize:"20px"}}>
            Helping farmers manage livestock, track animal health,
            and improve dairy productivity with modern technology.
          </p>
        </div>


        <div className="footer-section" style={{marginLeft:"auto"}}>
          <h3>Contact</h3>
          <p style={{fontSize:"16px"}}>📧 Email: support@cattlecloud.com</p>
          <p style={{fontSize:"16px"}}>📞 Phone: +91 9876543210</p>
          <p style={{fontSize:"16px"}}>🌐 Location: India</p>
        </div>

      </div>

      <div className="footer-bottom">
        <p>© 2026 CattleCloud | Animal Husbandry Management System</p>
      </div>
    </footer>
  );
}