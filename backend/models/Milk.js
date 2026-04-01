import mongoose from "mongoose";

const milkSchema = new mongoose.Schema({
  animalId: String,
  quantity: String,
  date: String
}, { timestamps: true });

const Milk = mongoose.model("Milk", milkSchema);

export default Milk;