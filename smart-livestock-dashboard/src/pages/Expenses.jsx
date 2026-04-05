// Importing React and useState hook
import React, { useState, useEffect } from "react";

export default function Expenses() {

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

  // ✅ FETCH FROM BACKEND
 useEffect(() => {
  const fetchData = async () => {
    try {
      const res = await fetch("http://localhost:5000/api/expenses", {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("token")
        }
      });

      const data = await res.json();

      setExpenses(Array.isArray(data) ? data : []); // ✅ FIX

    } catch (err) {
      console.error(err);
      setExpenses([]);
    }
  };

  fetchData();
}, []);

  // Add Transaction
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

    // ✅ SEND TO BACKEND
    await fetch("http://localhost:5000/api/expenses", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newRecord)
    });

    // ✅ REFRESH DATA
    const res = await fetch("http://localhost:5000/api/expenses");
    const data = await res.json();

    setRecords(data);

    setType("");
    setCategory("");
    setAmount("");
    setDate("");
    setDescription("");
  };

  // Delete transaction
  const deleteRecord = async (id) => {

    await fetch(`http://localhost:5000/api/expenses/${id}`, {
      method: "DELETE"
    });

    const res = await fetch("http://localhost:5000/api/expenses");
    const data = await res.json();

    setRecords(data);
  };

  // Calculations
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
        Farm Transactions
      </h2>

      {/* Form */}
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
          <label>Type</label>
          <select
            value={type}
            onChange={(e)=>{
              setType(e.target.value);
              setCategory("");
            }}
          >
            <option value="">Select Type</option>
            <option>Expense</option>
            <option>Profit</option>
          </select>
        </div>

        <div>
          <label>Category</label>
          <select
            value={category}
            onChange={(e)=>setCategory(e.target.value)}
          >
            <option value="">Select Category</option>

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
          <label>Amount (₹)</label>
          <input
            type="number"
            value={amount}
            onChange={(e)=>setAmount(e.target.value)}
          />
        </div>

        <div>
          <label>Date</label>
          <input
            type="date"
            value={date}
            onChange={(e)=>setDate(e.target.value)}
          />
        </div>

        <div>
          <label>Description</label>
          <input
            placeholder="Details"
            value={description}
            onChange={(e)=>setDescription(e.target.value)}
          />
        </div>

        <button type="submit">
          Add
        </button>

      </form>

      {/* Table */}
      <table className="styled-table">

        <thead>
          <tr>
            <th>Type</th>
            <th>Category</th>
            <th>Amount</th>
            <th>Date</th>
            <th>Description</th>
            <th>Action</th>
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
                  Delete
                </button>
              </td>

            </tr>
          ))}

          <tr style={{color:"black",fontWeight:"bold", background:"#f1f2f6"}}>
            <td>Totals</td>
            <td>Expenses ₹{totalExpenses}</td>
            <td>Profit ₹{totalProfit}</td>
            <td colSpan="3">
              Net Profit / Loss : ₹{netProfitLoss}
            </td>
          </tr>

        </tbody>

      </table>

      <div style={{
        marginTop:"10px",
        fontWeight:"bold",
        color: netProfitLoss >= 0 ? "green" : "red"
      }}>
        {netProfitLoss >= 0
          ? `Farm Profit: ₹${netProfitLoss}`
          : `Farm Loss: ₹${Math.abs(netProfitLoss)}`
        }
      </div>

    </div>
  );
}