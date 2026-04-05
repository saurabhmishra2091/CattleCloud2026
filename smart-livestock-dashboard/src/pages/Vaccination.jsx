// Importing React and useState hook
import React, { useState, useEffect } from "react";

export default function Vaccination() {

  const [date, setDate] = useState("");
  const [animalId, setAnimalId] = useState("");
  const [breed, setBreed] = useState("");
  const [vaccineName, setVaccineName] = useState("");

  const [records, setRecords] = useState([]);
  const [error, setError] = useState("");

  const vaccineRules = {
    FMD: 6,
    HS: 12,
    BQ: 12,
    Brucellosis: 0,
    Theileriosis: 0,
    Anthrax: 12
  };

  // ✅ FETCH FROM BACKEND (FIXED)
  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch("http://localhost:5000/api/vaccinations", {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token")
          }
        });

        const data = await res.json();

        setRecords(Array.isArray(data) ? data : []); // ✅ FIX

      } catch (err) {
        console.error(err);
        setRecords([]); // ✅ SAFETY
      }
    };

    fetchData();
  }, []);

  // Add Vaccination
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!date || !animalId || !breed || !vaccineName) return;

    const vaccine = vaccineName.trim();

    if (!vaccineRules.hasOwnProperty(vaccine)) {
      setError("Invalid vaccine name! Allowed: FMD, HS, BQ, Brucellosis, Theileriosis, Anthrax");
      return;
    }

    setError("");

    const selectedDate = new Date(date);
    const months = vaccineRules[vaccine];

    let upcomingDate = "No booster";

    if (months > 0) {
      const nextDate = new Date(selectedDate);
      nextDate.setMonth(nextDate.getMonth() + months);
      upcomingDate = nextDate.toISOString().split("T")[0];
    }

    const newRecord = {
      animalId,
      breed,
      vaccineName: vaccine,
      date,
      upcomingDate
    };

    // ✅ SEND TO BACKEND (FIXED)
    await fetch("http://localhost:5000/api/vaccinations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + localStorage.getItem("token")
      },
      body: JSON.stringify(newRecord)
    });

    // ✅ REFRESH DATA (FIXED)
    const res = await fetch("http://localhost:5000/api/vaccinations", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token")
      }
    });

    const data = await res.json();
    setRecords(Array.isArray(data) ? data : []);

    setDate("");
    setAnimalId("");
    setBreed("");
    setVaccineName("");
  };

  // Delete vaccination
  const deleteVaccination = async (id) => {

    await fetch(`http://localhost:5000/api/vaccinations/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token")
      }
    });

    const res = await fetch("http://localhost:5000/api/vaccinations", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token")
      }
    });

    const data = await res.json();
    setRecords(Array.isArray(data) ? data : []);
  };

  // ✅ SAFE REMINDERS
  const safeRecords = Array.isArray(records) ? records : [];

  const reminders = safeRecords.filter(v => {

    if(!v.upcomingDate || v.upcomingDate === "No booster") return false;

    const diff = (new Date(v.upcomingDate) - new Date()) / (1000*60*60*24);

    return diff <= 3;

  });

  return (
    <div>

      <h2 style={{fontSize:"32px",textAlign:"center",marginBottom:"25px"}}>
        Vaccination Schedule
      </h2>

      {reminders.length > 0 && (
        <div style={{
          background:"#ffe5e5",
          padding:"10px",
          marginBottom:"15px",
          borderRadius:"6px"
        }}>
          ⚠️ {reminders.length} vaccination(s) due within 3 days
        </div>
      )}

      <form
        className="form-grid"
        onSubmit={handleSubmit}
        style={{
          display:"flex",
          alignItems:"flex-end",
          gap:"15px",
          padding:"20px",
          borderRadius:"10px",
          boxShadow:"0 4px 10px rgba(0,0,0,0.1)",
          marginBottom:"20px",
          background:"white",
          color:"black"
        }}
      >
          
        <div>
          <label>Animal ID</label>
          <input value={animalId} onChange={(e)=>setAnimalId(e.target.value)} />
        </div>

        <div>
          <label>Breed</label>
          <input value={breed} onChange={(e)=>setBreed(e.target.value)} />
        </div>

        <div>
          <label>Vaccine Name</label>
          <select value={vaccineName} onChange={(e)=>setVaccineName(e.target.value)}>
            <option value="">Select Vaccine</option>
            <option value="FMD">FMD</option>
            <option value="HS">HS</option>
            <option value="BQ">BQ</option>
            <option value="Brucellosis">Brucellosis</option>
            <option value="Theileriosis">Theileriosis</option>
            <option value="Anthrax">Anthrax</option>
          </select>
        </div>

        <div>
          <label>Date of Vaccination</label>
          <input type="date" value={date} onChange={(e)=>setDate(e.target.value)} />
        </div>

        <button type="submit">Add</button>

      </form>

      {error && <p style={{color:"red"}}>{error}</p>}

      <table className="styled-table">

        <thead>
          <tr>
            <th>Animal ID</th>
            <th>Breed</th>
            <th>Vaccine</th>
            <th>Date</th>
            <th>Next Due</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>

          {(Array.isArray(records) ? records : []).map((record)=>(
            <tr key={record._id} style={{color:"black",background:"lightgray"}}>

              <td>{record.animalId}</td>
              <td>{record.breed}</td>
              <td>{record.vaccineName}</td>
              <td>{record.date}</td>
              <td>{record.upcomingDate}</td>

              <td>
                <button onClick={()=>deleteVaccination(record._id)}>
                  Delete
                </button>
              </td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}