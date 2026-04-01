import express from "express";
import Milk from "../models/Milk.js";

const router = express.Router();

// Add milk
router.post("/", async (req, res) => {
  try {
    const milk = new Milk(req.body);
    const saved = await milk.save();
    res.json(saved);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Get all milk records
router.get("/", async (req, res) => {
  try {
    const data = await Milk.find();
    res.json(data);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});
router.delete("/:id", async (req, res) => {
  try {
    await Milk.findByIdAndDelete(req.params.id);
    res.json({ message: "Deleted" });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

export default router;