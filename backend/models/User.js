import mongoose from "mongoose";

const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  image: String
});

export default mongoose.model("User", userSchema);