// Importing React and useState hook
import React, { useState, useEffect } from "react";

// ✅ Import translations
import { text } from "../utils/translations";

export default function Expenses({ lang }) {

  // ✅ SAFE FALLBACK
  const t = text[lang] || text["en"];

  const [type, setType] = useState("");
  const [category, setCategory] = useState("");
  const [amount, setAmount] = useState("");
  const [date, setDate] = useState("");
  const [description, setDescription] = useState("");

  const [records, setRecords] = useState([]);

  // ✅ COMMON INPUT STYLE
  const inputStyle = {
    width: "100%",
    height: "40px",
    padding: "8px",
    borderRadius: "5px",
    border: "1px solid #ccc",
    boxSizing: "border-box"
  };

  const expenseCategories = [
    "Feed",
    "Veterinary",
    "Labor",
    "Equipment",
    "Maintenance",
    "Breeding",
    "Animal Purchase"
  ];

  const profitCategories = [
    "Milk Sale",
    "Dairy Products",
    "Animal Sale",
    "Manure Sale",
    "Government Subsidy"
  ];

  // ✅ FETCH RECORDS
  const fetchRecords = async () => {
    try {
      const res = await fetch("http://localhost:5000/api/expenses", {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("token")
        }
      });

      const data = await res.json();

      setRecords(Array.isArray(data) ? data : []);

    } catch (err) {
      console.error("Fetch Error:", err);
      setRecords([]);
    }
  };

  // ✅ LOAD DATA
  useEffect(() => {
    fetchRecords();
  }, []);

  // ✅ ADD RECORD
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!type || !category || !amount || !date) {
      alert("Please fill all required fields");
      return;
    }

    const newRecord = {
      type,
      category,
      amount: Number(amount),
      date,
      description
    };

    try {

      await fetch("http://localhost:5000/api/expenses", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + localStorage.getItem("token")
        },
        body: JSON.stringify(newRecord)
      });

      // ✅ REFRESH TABLE
      await fetchRecords();

      // ✅ CLEAR FORM
      setType("");
      setCategory("");
      setAmount("");
      setDate("");
      setDescription("");

    } catch (err) {
      console.error("Add Error:", err);
    }
  };

  // ✅ DELETE RECORD
  const deleteRecord = async (id) => {

    try {

      await fetch(`http://localhost:5000/api/expenses/${id}`, {
        method: "DELETE",
        headers: {
          Authorization: "Bearer " + localStorage.getItem("token")
        }
      });

      // ✅ REFRESH TABLE
      await fetchRecords();

    } catch (err) {
      console.error("Delete Error:", err);
    }
  };

  // ✅ CALCULATIONS
  const totalExpenses = records
    .filter(r => r.type === "Expense")
    .reduce((sum, r) => sum + Number(r.amount), 0);

  const totalProfit = records
    .filter(r => r.type === "Profit")
    .reduce((sum, r) => sum + Number(r.amount), 0);

  const netProfitLoss = totalProfit - totalExpenses;

  return (
    <div style={{ padding: "20px" }}>

      <h2
        style={{
          fontSize: "32px",
          textAlign: "center",
          marginBottom: "20px"
        }}
      >
        {t.transactions}
      </h2>

      <form
        onSubmit={handleSubmit}
        style={{
          display: "flex",
          gap: "15px",
          alignItems: "flex-end",
          padding: "20px",
          borderRadius: "10px",
          boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
          marginBottom: "20px",
          background: "white",
          color: "black",
          flexWrap: "wrap"
        }}
      >

        {/* TYPE */}
        <div style={{ minWidth: "220px" }}>
          <label>{t.type}</label>
          <br />

          <select
            value={type}
            onChange={(e) => {
              setType(e.target.value);
              setCategory("");
            }}
            style={inputStyle}
          >
            <option value="">{t.selectType}</option>
            <option value="Expense">{t.expense}</option>
            <option value="Profit">{t.profit}</option>
          </select>
        </div>

        {/* CATEGORY */}
        <div style={{ minWidth: "220px" }}>
          <label>{t.category}</label>
          <br />

          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            style={inputStyle}
          >
            <option value="">{t.selectCategory}</option>

            {type === "Expense" &&
              expenseCategories.map((c, i) => (
                <option key={i} value={c}>
                  {c}
                </option>
              ))
            }

            {type === "Profit" &&
              profitCategories.map((c, i) => (
                <option key={i} value={c}>
                  {c}
                </option>
              ))
            }

          </select>
        </div>

        {/* AMOUNT */}
        <div style={{ minWidth: "220px" }}>
          <label>{t.amount} (₹)</label>
          <br />

          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            style={inputStyle}
          />
        </div>

        {/* DATE */}
        <div style={{ minWidth: "220px" }}>
          <label>{t.date}</label>
          <br />

          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            style={inputStyle}
          />
        </div>

        {/* DESCRIPTION */}
        <div style={{ minWidth: "220px" }}>
          <label>{t.description}</label>
          <br />

          <input
            placeholder={t.details}
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            style={inputStyle}
          />
        </div>

        {/* BUTTON */}
        <div>
          <button
            type="submit"
            style={{
              height: "40px",
              padding: "0 20px",
              border: "none",
              borderRadius: "5px",
              cursor: "pointer"
            }}
          >
            {t.add}
          </button>
        </div>

      </form>

      {/* TABLE */}
      <div className="table-wrapper">

        <table className="styled-table">

          <thead>
            <tr>
              <th>{t.type}</th>
              <th>{t.category}</th>
              <th>{t.amount}</th>
              <th>{t.date}</th>
              <th>{t.description}</th>
              <th>{t.action}</th>
            </tr>
          </thead>

          <tbody>

            {records.length > 0 ? (
              records.map((r) => (
                <tr
                  key={r._id}
                  style={{
                    color: "black",
                    background: "lightgray"
                  }}
                >

                  <td>{r.type}</td>
                  <td>{r.category}</td>
                  <td>₹{r.amount}</td>
                  <td>{r.date}</td>
                  <td>{r.description}</td>

                  <td>
                    <button
                      onClick={() => deleteRecord(r._id)}
                      style={{
                        background: "red",
                        color: "white",
                        border: "none",
                        padding: "5px 10px",
                        borderRadius: "5px",
                        cursor: "pointer"
                      }}
                    >
                      {t.delete}
                    </button>
                  </td>

                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6" style={{ textAlign: "center" }}>
                  No Records Found
                </td>
              </tr>
            )}

            {/* TOTALS */}
            <tr
              style={{
                color: "black",
                fontWeight: "bold",
                background: "#f1f2f6"
              }}
            >
              <td>{t.totals}</td>
              <td>{t.expenses} ₹{totalExpenses}</td>
              <td>{t.profit} ₹{totalProfit}</td>
              <td colSpan="3">
                {t.net} : ₹{netProfitLoss}
              </td>
            </tr>

          </tbody>

        </table>

      </div>

      {/* PROFIT / LOSS */}
      <div
        style={{
          marginTop: "10px",
          fontWeight: "bold",
          color: netProfitLoss >= 0 ? "green" : "red"
        }}
      >
        {netProfitLoss >= 0
          ? `${t.farmProfit}: ₹${netProfitLoss}`
          : `${t.farmLoss}: ₹${Math.abs(netProfitLoss)}`
        }
      </div>

    </div>
  );
}