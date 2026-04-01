import express from "express";
import Animal from "../models/Animal.js";

const router = express.Router();

// ✅ Add Animal
router.post("/", async (req, res) => {
  try {
    const animal = new Animal({
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

// ✅ Get All Animals
// ✅ FIXED
router.get("/", async (req, res) => {
  try {
    const animals = await Animal.find();

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

// ✅ Get Single Animal
router.get("/:id", async (req, res) => {
  try {
    const animal = await Animal.findById(req.params.id);
    res.json(animal);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// ✅ Delete Animal
router.delete("/:id", async (req, res) => {
  try {
    await Animal.findByIdAndDelete(req.params.id);
    res.json({ message: "Animal deleted" });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

export default router;