// Importing React and useState hook
import React, { useState, useEffect } from "react";

// ✅ Import translations
import { text } from "../utils/translations";

export default function Milk({ lang }) {

  // ✅ SAFE FALLBACK
  const t = text[lang] || text["en"];

  const [animalId, setAnimalId] = useState("");
  const [date, setDate] = useState("");
  const [quantity, setQuantity] = useState("");

  const [records, setRecords] = useState([]);

  const milkPrice = 70;

  // ✅ COMMON INPUT STYLE
  const inputStyle = {
    width: "100%",
    height: "40px",
    padding: "8px",
    borderRadius: "5px",
    border: "1px solid #ccc",
    boxSizing: "border-box"
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch("http://localhost:5000/api/milk", {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token")
          }
        });

        const data = await res.json();
        setRecords(Array.isArray(data) ? data : []);

      } catch (err) {
        console.error(err);
        setRecords([]);
      }
    };

    fetchData();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!animalId || !date || !quantity) return;

    const newRecord = {
      animalId,
      date,
      quantity: Number(quantity)
    };

    await fetch("http://localhost:5000/api/milk", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + localStorage.getItem("token")
      },
      body: JSON.stringify(newRecord)
    });

    const res = await fetch("http://localhost:5000/api/milk", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token")
      }
    });

    const data = await res.json();
    setRecords(Array.isArray(data) ? data : []);

    setAnimalId("");
    setDate("");
    setQuantity("");
  };

  const deleteMilk = async (id) => {

    await fetch(`http://localhost:5000/api/milk/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token")
      }
    });

    const res = await fetch("http://localhost:5000/api/milk", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token")
      }
    });

    const data = await res.json();
    setRecords(Array.isArray(data) ? data : []);
  };

  const safeRecords = Array.isArray(records) ? records : [];

  const totalMilk = safeRecords.reduce(
    (sum, r) => sum + Number(r.quantity),
    0
  );

  const totalIncome = totalMilk * milkPrice;

  const avgMilk = totalMilk / (safeRecords.length || 1);

  return (
    <div style={{ padding: "20px" }}>

      <h2
        style={{
          fontSize: "32px",
          textAlign: "center",
          marginBottom: "20px"
        }}
      >
        {t.milkProductionTitle}
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

        {/* Animal ID */}
        <div style={{ minWidth: "220px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>
            {t.animalId}
          </label>

          <input
            placeholder={t.animalId}
            value={animalId}
            onChange={(e) => setAnimalId(e.target.value)}
            style={inputStyle}
          />
        </div>

        {/* Date */}
        <div style={{ minWidth: "220px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>
            {t.date}
          </label>

          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            style={inputStyle}
          />
        </div>

        {/* Milk Quantity */}
        <div style={{ minWidth: "220px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>
            {t.milkQuantity}
          </label>

          <input
            type="number"
            placeholder={t.litres}
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            style={inputStyle}
          />
        </div>

        {/* Button */}
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

      <div className="table-wrapper">

        <table className="styled-table">

          <thead>
            <tr>
              <th>{t.animalId}</th>
              <th>{t.date}</th>
              <th>{t.milk}</th>
              <th>{t.income}</th>
              <th>{t.action}</th>
            </tr>
          </thead>

          <tbody>

            {(Array.isArray(records) ? records : []).map((record) => (
              <tr
                key={record._id}
                style={{
                  color: "black",
                  background: "lightgray"
                }}
              >

                <td style={{ textAlign: "center" }}>
                  {record.animalId}
                </td>

                <td style={{ textAlign: "center" }}>
                  {record.date}
                </td>

                <td style={{ textAlign: "center" }}>
                  {record.quantity}
                </td>

                <td style={{ textAlign: "center" }}>
                  ₹{record.quantity * milkPrice}
                </td>

                <td style={{ textAlign: "center" }}>

                  <button
                    onClick={() => deleteMilk(record._id)}
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
            ))}

            <tr
              style={{
                color: "black",
                fontWeight: "bold",
                background: "#f1f2f6",
                textAlign: "center"
              }}
            >
              <td colSpan="2">{t.total}</td>
              <td>{totalMilk} L</td>
              <td>₹{totalIncome}</td>
              <td></td>
            </tr>

          </tbody>

        </table>

      </div>

      <div
        style={{
          marginTop: "10px",
          fontWeight: "bold"
        }}
      >
        {t.averageMilk}: {avgMilk.toFixed(2)} L
      </div>

    </div>
  );
}