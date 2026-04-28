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

 useEffect(() => {
  const fetchData = async () => {
    try {
      const res = await fetch("http://localhost:5000/api/expenses", {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("token")
        }
      });

      const data = await res.json();

      // ✅ FIXED
      setRecords(Array.isArray(data) ? data : []);

    } catch (err) {
      console.error(err);

      // ✅ FIXED
      setRecords([]);
    }
  };

  fetchData();
}, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!type || !category || !amount || !date) return;

    const newRecord = {
      type,
      category,
      amount: Number(amount),
      date,
      description
    };

    await fetch("http://localhost:5000/api/expenses", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newRecord)
    });

    const res = await fetch("http://localhost:5000/api/expenses");
    const data = await res.json();

    setRecords(data);

    setType("");
    setCategory("");
    setAmount("");
    setDate("");
    setDescription("");
  };

  const deleteRecord = async (id) => {

    await fetch(`http://localhost:5000/api/expenses/${id}`, {
      method: "DELETE"
    });

    const res = await fetch("http://localhost:5000/api/expenses");
    const data = await res.json();

    setRecords(data);
  };

  const totalExpenses = records
    .filter(r => r.type === "Expense")
    .reduce((sum, r) => sum + Number(r.amount), 0);

  const totalProfit = records
    .filter(r => r.type === "Profit")
    .reduce((sum, r) => sum + Number(r.amount), 0);

  const netProfitLoss = totalProfit - totalExpenses;

  return (
    <div style={{ padding: "20px" }}>

      <h2 style={{
        fontSize: "32px",
        textAlign: "center",
        marginBottom: "20px"
      }}>
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
          background:"white",
          color:"black"
        }}
      >

        <div>
          <label>{t.type}</label>
          <select
            value={type}
            onChange={(e)=>{
              setType(e.target.value);
              setCategory("");
            }}
          >
            <option value="">{t.selectType}</option>
            <option>{t.expense}</option>
            <option>{t.profit}</option>
          </select>
        </div>

        <div>
          <label>{t.category}</label>
          <select
            value={category}
            onChange={(e)=>setCategory(e.target.value)}
          >
            <option value="">{t.selectCategory}</option>

            {type === "Expense" &&
              expenseCategories.map((c,i)=>(
                <option key={i}>{c}</option>
              ))
            }

            {type === "Profit" &&
              profitCategories.map((c,i)=>(
                <option key={i}>{c}</option>
              ))
            }

          </select>
        </div>

        <div>
          <label>{t.amount} (₹)</label>
          <input
            type="number"
            value={amount}
            onChange={(e)=>setAmount(e.target.value)}
          />
        </div>

        <div>
          <label>{t.date}</label>
          <input
            type="date"
            value={date}
            onChange={(e)=>setDate(e.target.value)}
          />
        </div>

        <div>
          <label>{t.description}</label>
          <input
            placeholder={t.details}
            value={description}
            onChange={(e)=>setDescription(e.target.value)}
          />
        </div>

        <button type="submit">
          {t.add}
        </button>

      </form>
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

          {records.map((r)=>(
            <tr key={r._id} style={{color:"black",background:"lightgray"}}>

              <td>{r.type}</td>
              <td>{r.category}</td>
              <td>₹{r.amount}</td>
              <td>{r.date}</td>
              <td>{r.description}</td>

              <td>
                <button onClick={()=>deleteRecord(r._id)}>
                  {t.delete}
                </button>
              </td>

            </tr>
          ))}

          <tr style={{color:"black",fontWeight:"bold", background:"#f1f2f6"}}>
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
      <div style={{
        marginTop:"10px",
        fontWeight:"bold",
        color: netProfitLoss >= 0 ? "green" : "red"
      }}>
        {netProfitLoss >= 0
          ? `${t.farmProfit}: ₹${netProfitLoss}`
          : `${t.farmLoss}: ₹${Math.abs(netProfitLoss)}`
        }
      </div>

    </div>
  );
}