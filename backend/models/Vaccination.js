import mongoose from "mongoose";

const vaccinationSchema = new mongoose.Schema({
  animalId: String,
  vaccineName: String,
  date: String,
  upcomingDate: String
}, { timestamps: true });

const Vaccination = mongoose.model("Vaccination", vaccinationSchema);

export default Vaccination;