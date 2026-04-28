import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { useNavigate } from "react-router-dom";
import { text } from "../utils/translations";

export default function Landing({lang, setLang}) {
  const navigate = useNavigate();

  // ✅ translation object
  const t = text[lang] || text["en"];

  return (
    <>
      <Navbar lang={lang} setLang={setLang} />

      {/* HERO SECTION */}
      <section className="hero">
        <div className="hero-container">

          <div className="hero-left">
            <h1>
              {t.heroTitle1} <br />
              <span>{t.heroTitle2}</span>
            </h1>

            <p className="tagline">
              {t.heroTagline}
            </p>

            <div className="hero-actions">
              <button 
                className="btn-primary"
                onClick={() => navigate("/register")}
              >
                {t.getStarted}
              </button>

              <button
                className="btn-outline"
                onClick={() => window.open("https://youtu.be/XbKd-xIJSKY")}
              >
                {t.watchDemo}
              </button>

              <button
                className="btn-primary"
                onClick={() =>
                  document
                    .getElementById("features")
                    .scrollIntoView({ behavior: "smooth" })
                }
              >
                {t.exploreFeatures}
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
        <div>{t.farms}</div>
        <div>{t.milkTracked}</div>
        <div>{t.farmers}</div>
      </section>

      {/* TRUSTED */}
      <section className="trusted">
        <p>{t.trustedText}</p>

        <div className="trusted-logos">
          <span>{t.dairy}</span>
          <span>{t.agriculture}</span>
          <span>{t.milkProducers}</span>
          <span>{t.community}</span>
        </div>
      </section>

      {/* FEATURES */}
      <section id="features" className="features">
        <h2>{t.keyFeatures}</h2>
        <p className="subtitle">{t.empowering}</p>

        <div className="features-grid">

          <div className="feature-card">
            🐄
            <h3>{t.animalReg}</h3>
            <p>{t.animalRegDesc}</p>
          </div>

          <div className="feature-card">
            💉
            <h3>{t.vaccineTrack}</h3>
            <p>{t.vaccineTrackDesc}</p>
          </div>

          <div className="feature-card">
            🥛
            <h3>{t.milkProd}</h3>
            <p>{t.milkProdDesc}</p>
          </div>

          <div className="feature-card">
            🐎
            <h3>{t.breeding}</h3>
            <p>{t.breedingDesc}</p>
          </div>

          <div className="feature-card">
            👨‍⚕️
            <h3>{t.vet}</h3>
            <p>{t.vetDesc}</p>
          </div>

          <div className="feature-card">
            📊
            <h3>{t.expense}</h3>
            <p>{t.expenseDesc}</p>
          </div>

        </div>
      </section>

      {/* DASHBOARD PREVIEW */}
      <section id="dashboard" className="dashboard-preview">

        <h2>{t.dashboardTitle}</h2>
        <p>{t.dashboardDesc}</p>

        <img
          src="https://images.unsplash.com/photo-1551288049-bebda4e38f71"
          alt="Dashboard"
        />

      </section>

      {/* BENEFITS */}
      <section className="benefits">

        <h2>{t.whyFarmers}</h2>

        <div className="benefit-grid">

          <div>
            ⚡
            <h3>{t.saveTime}</h3>
            <p>{t.noPaper}</p>
          </div>

          <div>
            📈
            <h3>{t.increaseMilk}</h3>
            <p>{t.improveYield}</p>
          </div>

          <div>
            💰
            <h3>{t.controlExpense}</h3>
            <p>{t.moneyTrack}</p>
          </div>

          <div>
            📱
            <h3>{t.accessAnywhere}</h3>
            <p>{t.mobileFriendly}</p>
          </div>

        </div>

      </section>

      {/* HOW IT WORKS */}
      <section id="how" className="how">
        <h2>{t.howItWorks}</h2>

        <div className="how-grid">

          <div className="how-card">
            <h3>{t.step1}</h3>
            <p>{t.step1Desc}</p>
          </div>

          <div className="how-card">
            <h3>{t.step2}</h3>
            <p>{t.step2Desc}</p>
          </div>

          <div className="how-card">
            <h3>{t.step3}</h3>
            <p>{t.step3Desc}</p>
          </div>

        </div>
      </section>

      {/* TESTIMONIAL */}
      <section className="testimonial">

        <div className="testimonial-box">

          <h4>⭐⭐⭐⭐⭐</h4>

          <p>{t.testimonial}</p>

          <strong>{t.author}</strong>

          <div className="hero-buttons">
            <button 
              className="btn-primary"
              onClick={() => navigate("/register")}
            >
              {t.getStarted}
            </button>

            <button
              className="btn-outline"
              onClick={() => window.open("https://youtu.be/XbKd-xIJSKY")}
            >
              {t.watchDemo}
            </button>
          </div>

        </div>

      </section>

      {/* FAQ */}
      <section className="faq">

        <h2>{t.faq}</h2>

        <div className="faq-item">
          <h4>{t.q1}</h4>
          <p>{t.a1}</p>
        </div>

        <div className="faq-item">
          <h4>{t.q2}</h4>
          <p>{t.a2}</p>
        </div>

      </section>

      {/* FINAL CTA */}
      <section className="cta">

        <h2>{t.ctaTitle}</h2>

        <p>{t.ctaDesc}</p>

        <button 
          className="btn-primary"
          onClick={() => navigate("/register")}
        >
          {t.startFree}
        </button>

      </section>

      <Footer lang={lang} />
    </>
  );
}