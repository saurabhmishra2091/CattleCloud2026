import mongoose from "mongoose";

const expenseSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true }, // ✅

  type: String,
  category: String,
  amount: Number,
  date: String,
  description: String
}, { timestamps: true });

export default mongoose.model("Expense", expenseSchema);