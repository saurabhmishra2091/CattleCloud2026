import express from "express";
import Milk from "../models/Milk.js";
import { protect } from "../middleware/authMiddleware.js";

const router = express.Router();

// ✅ ADD MILK
router.post("/", protect, async (req, res) => {
  try {
    const milk = new Milk({
      ...req.body,
      user: req.user.id   // ✅ LINK USER
    });

    const saved = await milk.save();
    res.json(saved);

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// ✅ GET MILK (ONLY USER DATA)
router.get("/", protect, async (req, res) => {
  try {
    const data = await Milk.find({ user: req.user.id }); // ✅ FILTER
    res.json(data);

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// ✅ DELETE
router.delete("/:id", protect, async (req, res) => {
  try {
    await Milk.findOneAndDelete({
      _id: req.params.id,
      user: req.user.id   // ✅ SECURITY
    });

    res.json({ message: "Deleted" });

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

export default router;