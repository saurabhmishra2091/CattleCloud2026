import mongoose from "mongoose";

const milkSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true }, // ✅

  animalId: String,
  date: String,
  quantity: Number
}, { timestamps: true });

export default mongoose.model("Milk", milkSchema);