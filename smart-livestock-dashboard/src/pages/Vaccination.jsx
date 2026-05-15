// Importing React and useState hook
import React, { useState, useEffect } from "react";

// ✅ Import translations
import { text } from "../utils/translations";

export default function Vaccination({ lang }) {
  // ✅ SAFE FALLBACK
  const t = text[lang] || text["en"];

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
    Anthrax: 12,
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch("http://localhost:5000/api/vaccinations", {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token"),
          },
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

    if (!date || !animalId || !breed || !vaccineName) return;

    const vaccine = vaccineName.trim();

    if (!vaccineRules.hasOwnProperty(vaccine)) {
      setError(t.invalidVaccine);
      return;
    }

    setError("");

    const selectedDate = new Date(date);
    const months = vaccineRules[vaccine];

    let upcomingDate = t.noBooster;

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
      upcomingDate,
    };

    await fetch("http://localhost:5000/api/vaccinations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
      body: JSON.stringify(newRecord),
    });

    const res = await fetch("http://localhost:5000/api/vaccinations", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });

    const data = await res.json();
    setRecords(Array.isArray(data) ? data : []);

    setDate("");
    setAnimalId("");
    setBreed("");
    setVaccineName("");
  };

  const deleteVaccination = async (id) => {
    await fetch(`http://localhost:5000/api/vaccinations/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });

    const res = await fetch("http://localhost:5000/api/vaccinations", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });

    const data = await res.json();
    setRecords(Array.isArray(data) ? data : []);
  };

  const safeRecords = Array.isArray(records) ? records : [];

  const reminders = safeRecords.filter((v) => {
    if (!v.upcomingDate || v.upcomingDate === t.noBooster) return false;

    const diff =
      (new Date(v.upcomingDate) - new Date()) / (1000 * 60 * 60 * 24);

    return diff <= 3;
  });

  return (
    <div>
      <h2
        style={{ fontSize: "32px", textAlign: "center", marginBottom: "25px" }}
      >
        {t.vaccinationSchedule}
      </h2>

      {reminders.length > 0 && (
        <div
          style={{
            background: "#ffe5e5",
            padding: "10px",
            marginBottom: "15px",
            borderRadius: "6px",
          }}
        >
          ⚠️ {reminders.length} {t.dueVaccines}
        </div>
      )}

      <form
        className="form-grid"
        onSubmit={handleSubmit}
        style={{
          display: "flex",
          alignItems: "flex-end",
          gap: "15px",
          padding: "20px",
          borderRadius: "10px",
          boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
          marginBottom: "20px",
          background: "white",
          color: "black",
        }}
      >
        <div>
          <label>{t.animalId}</label>
          <input
            value={animalId}
            onChange={(e) => setAnimalId(e.target.value)}
          />
        </div>

        <div style={{ minWidth: "220px" }}>
          <label>{t.breed}</label>

          <select
            value={breed}
            onChange={(e) => setBreed(e.target.value)}
            style={{
              width: "100%",
              height: "38px",
              padding: "5px",
            }}
          >
            <option value="">Select Breed</option>

            <option value="Gir">Gir</option>
            <option value="Sahiwal">Sahiwal</option>
            <option value="Red Sindhi">Red Sindhi</option>
            <option value="Tharparkar">Tharparkar</option>
            <option value="HF Cross">HF Cross</option>
            <option value="Jersey">Jersey</option>
            <option value="Murrah Buffalo">Murrah Buffalo</option>
            <option value="Mehsana Buffalo">Mehsana Buffalo</option>
            <option value="Bhadawari Buffalo">Bhadawari Buffalo</option>
          </select>
        </div>

        <div style={{ minWidth: "220px" }}>
          <label>{t.vaccineName}</label>

          <select
            value={vaccineName}
            onChange={(e) => setVaccineName(e.target.value)}
            style={{
              width: "100%",
              height: "38px",
              padding: "5px",
            }}
          >
            <option value="">{t.selectVaccine}</option>
            <option value="FMD">FMD</option>
            <option value="HS">HS</option>
            <option value="BQ">BQ</option>
            <option value="Brucellosis">Brucellosis</option>
            <option value="Theileriosis">Theileriosis</option>
            <option value="Anthrax">Anthrax</option>
          </select>
        </div>

        <div>
          <label>{t.vaccinationDate}</label>
          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
          />
        </div>

        <button type="submit">{t.add}</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}
      <div className="table-wrapper">
        <table className="styled-table">
          <thead>
            <tr>
              <th>{t.animalId}</th>
              <th>{t.breed}</th>
              <th>{t.vaccine}</th>
              <th>{t.date}</th>
              <th>{t.nextDue}</th>
              <th>{t.action}</th>
            </tr>
          </thead>

          <tbody>
            {(Array.isArray(records) ? records : []).map((record) => (
              <tr
                key={record._id}
                style={{ color: "black", background: "lightgray" }}
              >
                <td>{record.animalId}</td>
                <td>{record.breed}</td>
                <td>{record.vaccineName}</td>
                <td>{record.date}</td>
                <td>{record.upcomingDate}</td>

                <td>
                  <button onClick={() => deleteVaccination(record._id)}>
                    {t.delete}
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
