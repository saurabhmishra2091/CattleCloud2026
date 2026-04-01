import express from "express";
import Vaccination from "../models/Vaccination.js";

const router = express.Router();

// ADD
router.post("/", async (req, res) => {
  try {
    const data = new Vaccination(req.body);
    const saved = await data.save();
    res.json(saved);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// GET
router.get("/", async (req, res) => {
  try {
    const data = await Vaccination.find();
    res.json(data);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// DELETE
router.delete("/:id", async (req, res) => {
  try {
    await Vaccination.findByIdAndDelete(req.params.id);
    res.json({ message: "Deleted" });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

export default router;