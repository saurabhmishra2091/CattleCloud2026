import express from "express";
import { protect } from "../middleware/authMiddleware.js";
import User from "../models/User.js";

const router = express.Router();

// ✅ GET PROFILE (UPDATED)
router.get("/profile", protect, async (req, res) => {
  try {
    const user = await User.findById(req.user.id).select("-password");

    res.json({
      name: user.name,
      email: user.email,
      image: user.image
    });

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// ✅ UPDATE PROFILE IMAGE
router.put("/upload", protect, async (req, res) => {
  try {
    const user = await User.findByIdAndUpdate(
      req.user.id,
      { image: req.body.image },
      { new: true }
    );

    res.json({
      message: "Image updated",
      image: user.image
    });

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

export default router;