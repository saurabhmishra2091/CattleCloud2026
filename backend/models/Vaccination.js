import mongoose from "mongoose";

const vaccinationSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true }, // ✅

  animalId: String,
  breed: String,
  vaccineName: String,
  date: String,
  upcomingDate: String
}, { timestamps: true });

export default mongoose.model("Vaccination", vaccinationSchema);