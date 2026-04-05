import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { useNavigate } from "react-router-dom";

export default function Landing() {
  const navigate = useNavigate();
  return (
    <>
      <Navbar />

      {/* HERO SECTION */}
      <section className="hero">
        <div className="hero-container">

          <div className="hero-left">
            <h1>
              Digitize Your Farm <br />
              <span>Maximize Your Profit</span>
            </h1>

            <p className="tagline">
              All-in-one platform to manage livestock, milk production,
              health tracking and farm expenses.
            </p>

            <div className="hero-actions">
              <button 
  className="btn-primary"
  onClick={() => navigate("/register")}
>
  Get Started
</button>

<button
  className="btn-outline"
  onClick={() => window.open("https://youtu.be/XbKd-xIJSKY")}
>
  Watch Demo
</button>

              <button
                className="btn-primary"
                onClick={() =>
                  document
                    .getElementById("features")
                    .scrollIntoView({ behavior: "smooth" })
                }
              >
                Explore Features
              </button>
            </div>
          </div>

          <div className="hero-right">
            <img
              src="https://images.unsplash.com/photo-1625246333195-78d9c38ad449"
              alt="Farm Dashboard"
            />
          </div>

        </div>
      </section>

      {/* STATS */}
      <section className="stats">
        <div>🐄 500+ Farms</div>
        <div>🥛 50K+ Liters Tracked</div>
        <div>👨‍🌾 1200 Farmers</div>
      </section>

      {/* TRUSTED */}
      <section className="trusted">
        <p>Trusted by farmers across India</p>

        <div className="trusted-logos">
          <span>🐄 Dairy Farms</span>
          <span>🌾 Smart Agriculture</span>
          <span>🥛 Milk Producers</span>
          <span>👨‍🌾 Farmer Communities</span>
        </div>
      </section>

      {/* FEATURES */}
      <section id="features" className="features">
        <h2>Key Features</h2>
        <p className="subtitle">Empowering Livestock Management</p>

        <div className="features-grid">

          <div className="feature-card">
            🐄
            <h3>Animal Registration</h3>
            <p>Create and manage livestock profiles.</p>
          </div>

          <div className="feature-card">
            💉
            <h3>Vaccination Tracking</h3>
            <p>Schedule and record vaccines.</p>
          </div>

          <div className="feature-card">
            🥛
            <h3>Milk Production</h3>
            <p>Monitor daily milk yield.</p>
          </div>

          <div className="feature-card">
            🐎
            <h3>Breeding Management</h3>
            <p>Track breeding cycles.</p>
          </div>

          <div className="feature-card">
            👨‍⚕️
            <h3>Vet Appointment</h3>
            <p>Book and manage vet visits.</p>
          </div>

          <div className="feature-card">
            📊
            <h3>Expense Analysis</h3>
            <p>Analyze costs and revenue.</p>
          </div>

        </div>
      </section>

      {/* DASHBOARD PREVIEW */}
      <section id="dashboard" className="dashboard-preview">

        <h2>Powerful Farm Dashboard</h2>
        <p>See all your farm data in one place</p>

        <img
          src="https://images.unsplash.com/photo-1551288049-bebda4e38f71"
          alt="Dashboard"
        />

      </section>

      {/* BENEFITS */}
      <section className="benefits">

        <h2>Why Farmers Love CattleCloud</h2>

        <div className="benefit-grid">

          <div>
            ⚡
            <h3>Save Time</h3>
            <p>No more paperwork</p>
          </div>

          <div>
            📈
            <h3>Increase Milk Production</h3>
            <p>Track and improve yield</p>
          </div>

          <div>
            💰
            <h3>Control Expenses</h3>
            <p>Know where your money goes</p>
          </div>

          <div>
            📱
            <h3>Access Anywhere</h3>
            <p>Mobile friendly farm management</p>
          </div>

        </div>

      </section>

      {/* HOW IT WORKS */}
      <section id="how" className="how">
        <h2>How It Works</h2>

        <div className="how-grid">

          <div className="how-card">
            <h3>1️⃣ Register Farm</h3>
            <p>Create your farm profile</p>
          </div>

          <div className="how-card">
            <h3>2️⃣ Add Animals</h3>
            <p>Enter livestock data</p>
          </div>

          <div className="how-card">
            <h3>3️⃣ Track & Analyze</h3>
            <p>Monitor farm performance</p>
          </div>

        </div>
      </section>

      {/* TESTIMONIAL */}
      <section className="testimonial">

        <div className="testimonial-box">

          <h4>⭐⭐⭐⭐⭐</h4>

          <p>
            "Since using CattleCloud I've increased milk production
            and saved hours of paperwork every week."
          </p>

          <strong>Sandeep Rathor — Dairy Farmer</strong>

          <div className="hero-buttons">
            <button 
  className="btn-primary"
  onClick={() => navigate("/register")}
>
  Get Started
</button>
            <button
  className="btn-outline"
  onClick={() => window.open("https://youtu.be/XbKd-xIJSKY")}
>
  Watch Demo
</button>
          </div>

        </div>

      </section>

      {/* FAQ */}
      <section className="faq">

        <h2>Frequently Asked Questions</h2>

        <div className="faq-item">
          <h4>Is CattleCloud free?</h4>
          <p>Yes, basic features are free for farmers.</p>
        </div>

        <div className="faq-item">
          <h4>Can I track milk production?</h4>
          <p>Yes, you can track daily milk records easily.</p>
        </div>

         <div className="faq-item">
          <h4>Can I manage multiple animals?</h4>
          <p>Yes, you can add and manage unlimited animals with complete records.</p>
        </div>

        <div className="faq-item">
          <h4>Does it support vaccination tracking?</h4>
          <p>Yes, vaccination reminders and history are included.</p>
        </div>

         <div className="faq-item">
          <h4>Does it provide profit analysis?</h4>
          <p>Yes, you can track expenses and income to analyze your farm's profit.</p>
        </div>

         <div className="faq-item">
          <h4>Is it suitable for small farmers?</h4>
          <p>Yes,it is designed for btoh small and large-scale farmers. </p>
        </div>

         <div className="faq-item">
          <h4>Can I export my data?</h4>
          <p>Yes, You can export reports for offline use and analysis.</p>
        </div>

         <div className="faq-item">
          <h4>Can I track individual animal performance?</h4>
          <p>Yes, each animal has a unique profile where you can track health, production, and breeding data. </p>
        </div>

         <div className="faq-item">
          <h4>Does CattleCloud support data backup?</h4>
          <p>Yes, your data is automatically backed up to prevent loss.</p>
        </div>

      </section>

      {/* FINAL CTA */}
      <section className="cta">

        <h2>Start Managing Your Farm Smarter Today</h2>

        <p>Join thousands of farmers using CattleCloud</p>

         <button 
  className="btn-primary"
  onClick={() => navigate("/register")}
>
  Start Free
</button>

      </section>

      <Footer />
    </>
  );
}