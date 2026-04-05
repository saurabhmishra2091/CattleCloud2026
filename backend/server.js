import dotenv from "dotenv";
dotenv.config();

import express from "express";
import mongoose from "mongoose";
import cors from "cors";

import authRoutes from "./routes/authRoutes.js";
import userRoutes from "./routes/userRoutes.js";
import animalRoutes from "./routes/animalRoutes.js";
import milkRoutes from "./routes/milkRoutes.js";
import vaccinationRoutes from "./routes/vaccinationRoutes.js";
import expenseRoutes from "./routes/expenseRoutes.js";


const app = express();

app.use(cors());
app.use(express.json({ limit: "10mb" }));

// ✅ MongoDB connection using .env
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB Connected ✅"))
  .catch(err => console.log(err));

// Routes
app.use("/api/auth", authRoutes);
app.use("/api/users", userRoutes);
app.use("/api/animals", animalRoutes);
app.use("/api/milk", milkRoutes);
app.use("/api/vaccinations", vaccinationRoutes);
app.use("/api/expenses", expenseRoutes);

// Test route
app.get("/", (req, res) => {
  res.send("Backend running 🚀");
});

// Server
app.listen(process.env.PORT, () => {
  console.log(`Server running on port ${process.env.PORT}`);
});