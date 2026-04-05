import express from "express";
import Vaccination from "../models/Vaccination.js";
import { protect } from "../middleware/authMiddleware.js";

const router = express.Router();

// ✅ ADD
router.post("/", protect, async (req, res) => {
  try {
    const data = new Vaccination({
      ...req.body,
      user: req.user.id   // ✅ LINK USER
    });

    const saved = await data.save();
    res.json(saved);

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// ✅ GET (ONLY USER DATA)
router.get("/", protect, async (req, res) => {
  try {
    const data = await Vaccination.find({ user: req.user.id }); // ✅ FILTER
    res.json(data);

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// ✅ DELETE
router.delete("/:id", protect, async (req, res) => {
  try {
    await Vaccination.findOneAndDelete({
      _id: req.params.id,
      user: req.user.id   // ✅ SECURITY
    });

    res.json({ message: "Deleted" });

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

export default router;