import express from "express";
import Expense from "../models/Expense.js";
import { protect } from "../middleware/authMiddleware.js";

const router = express.Router();

// ✅ ADD EXPENSE
router.post("/", protect, async (req, res) => {
  try {
    const expense = new Expense({
      ...req.body,
      user: req.user.id   // ✅ LINK USER
    });

    const saved = await expense.save();
    res.json(saved);

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// ✅ GET EXPENSES (ONLY USER DATA)
router.get("/", protect, async (req, res) => {
  try {
    const data = await Expense.find({ user: req.user.id }); // ✅ FILTER
    res.json(data);

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// ✅ DELETE
router.delete("/:id", protect, async (req, res) => {
  try {
    await Expense.findOneAndDelete({
      _id: req.params.id,
      user: req.user.id   // ✅ SECURITY
    });

    res.json({ message: "Deleted" });

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

export default router;