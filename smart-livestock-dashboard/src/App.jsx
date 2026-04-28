import { Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";

import PrivateRoute from "./components/PrivateRoute";
import Layout from "./components/layout";

import Landing from "./pages/Landing";
import Login from "./pages/Login";
import Register from "./pages/Register";
import FarmerDashboard from "./pages/FarmerDashboard";
import DepartmentDashboard from "./pages/DepartmentDashboard";
import Animal from "./pages/Animal";
import Milk from "./pages/Milk";
import Vaccination from "./pages/Vaccination";
import Expenses from "./pages/Expenses";
import ForgotPassword from "./pages/ForgotPassword";

export default function App() {

  // ✅ SAFE fallback (handles null/invalid values)
  const [lang, setLang] = useState(() => {
    const saved = localStorage.getItem("lang");
    return saved === "hi" || saved === "en" ? saved : "en";
  });

  useEffect(() => {
    localStorage.setItem("lang", lang);
  }, [lang]);

  return (
    <Routes>
      <Route path="/" element={<Landing lang={lang} setLang={setLang} />} />
      <Route path="/login" element={<Login lang={lang} setLang={setLang} />} />
      <Route path="/forgot-password" element={<ForgotPassword lang={lang} setLang={setLang} />} />
      <Route path="/register" element={<Register lang={lang} setLang={setLang} />} />

      <Route element={<PrivateRoute />}>
        <Route element={<Layout lang={lang} setLang={setLang} />}>

          <Route path="/farmer-dashboard" element={<FarmerDashboard lang={lang} />} />
          <Route path="/department-dashboard" element={<DepartmentDashboard lang={lang} />} />
          <Route path="/animals" element={<Animal lang={lang} />} />
          <Route path="/milk" element={<Milk lang={lang} />} />
          <Route path="/vaccination" element={<Vaccination lang={lang} />} />
          <Route path="/expenses" element={<Expenses lang={lang} />} />

        </Route>
      </Route>
    </Routes>
  );
}