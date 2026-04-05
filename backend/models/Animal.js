import mongoose from "mongoose";

const animalSchema = new mongoose.Schema(
  {
    // ✅ LINK TO USER (VERY IMPORTANT)
    user: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true
    },

    animalId: {
      type: String,
      required: true,
    },
    breed: {
      type: String,
      required: true,
    },
    age: {
      type: String,
    },
    gender: {
      type: String,
    },
    cost: {
      type: String,
    },
    health: {
      type: String,
    }
  },
  { timestamps: true }
);

const Animal = mongoose.model("Animal", animalSchema);

export default Animal;