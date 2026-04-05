import { Routes, Route } from "react-router-dom";
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
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />
      <Route path="/forgot-password" element={<ForgotPassword />} />
      <Route path="/register" element={<Register />} />

      <Route element={<PrivateRoute />}>
        <Route element={<Layout />}>
          
          <Route path="/farmer-dashboard" element={<FarmerDashboard />} />
          <Route path="/department-dashboard" element={<DepartmentDashboard />} />
          <Route path="/animals" element={<Animal />} />
          <Route path="/milk" element={<Milk />} />
          <Route path="/vaccination" element={<Vaccination />} />
          <Route path="/expenses" element={<Expenses />} />
        </Route>
      </Route>
    </Routes>
  );
}