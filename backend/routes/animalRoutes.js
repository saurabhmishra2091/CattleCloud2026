import express from "express";
import Animal from "../models/Animal.js";
import { protect } from "../middleware/authMiddleware.js"; // ✅ ADD

const router = express.Router();

// ✅ Add Animal (USER LINKED)
router.post("/", protect, async (req, res) => {
  try {
    const animal = new Animal({
      user: req.user.id,   // ✅ VERY IMPORTANT
      animalId: req.body.id,
      breed: req.body.breed,
      age: req.body.age,
      gender: req.body.gender,
      cost: req.body.cost,
      health: req.body.health
    });

    const savedAnimal = await animal.save();
    res.status(201).json(savedAnimal);

  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// ✅ Get All Animals (ONLY CURRENT USER DATA)
router.get("/", protect, async (req, res) => {
  try {
    const animals = await Animal.find({ user: req.user.id }); // ✅ FILTER

    const formatted = animals.map(a => ({
      id: a.animalId,
      breed: a.breed,
      age: a.age,
      gender: a.gender,
      cost: a.cost,
      health: a.health,
      _id: a._id
    }));

    res.json(formatted);

  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// ✅ Get Single Animal (OPTIONAL FILTER)
router.get("/:id", protect, async (req, res) => {
  try {
    const animal = await Animal.findOne({
      _id: req.params.id,
      user: req.user.id   // ✅ SECURITY
    });

    res.json(animal);

  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// ✅ Delete Animal (ONLY OWNER CAN DELETE)
router.delete("/:id", protect, async (req, res) => {
  try {
    await Animal.findOneAndDelete({
      _id: req.params.id,
      user: req.user.id   // ✅ SECURITY
    });

    res.json({ message: "Animal deleted" });

  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

export default router;