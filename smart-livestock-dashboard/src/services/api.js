// src/services/Api.js
import axios from "axios";

const Api = axios.create({
  baseURL: "https://api.example.com"
});

export const getData = () => Api.get("/data");
export const postData = data => Api.post("/data", data);

export default Api;