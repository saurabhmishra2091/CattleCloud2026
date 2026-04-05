// src/services/storage.js

// Animals
export const getAnimals = () => {
  return JSON.parse(localStorage.getItem("animals")) || [];
};

export const saveAnimals = (data) => {
  localStorage.setItem("animals", JSON.stringify(data));
};


// Milk Records
export const getMilkRecords = () => {
  return JSON.parse(localStorage.getItem("milkRecords")) || [];
};

export const saveMilkRecords = (data) => {
  localStorage.setItem("milkRecords", JSON.stringify(data));
};


// Vaccination Records
export const getVaccinations = () => {
  return JSON.parse(localStorage.getItem("vaccinations")) || [];
};

export const saveVaccinations = (data) => {
  localStorage.setItem("vaccinations", JSON.stringify(data));
};


// Expenses
export const getExpenses = () => {
  return JSON.parse(localStorage.getItem("expenses")) || [];
};

export const saveExpenses = (data) => {
  localStorage.setItem("expenses", JSON.stringify(data));
};


// Users
export const getUsers = () => {
  return JSON.parse(localStorage.getItem("users")) || [];
};

export const saveUsers = (data) => {
  localStorage.setItem("users", JSON.stringify(data));
};