import React, { useState, useEffect } from "react";

// ✅ Import translations
import { text } from "../utils/translations";

export default function Animal({ lang }) {

  // ✅ SAFE FALLBACK
  const t = text[lang] || text["en"];

  const [animals, setAnimals] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    const fetchAnimals = async () => {
      try {
        const res = await fetch("http://localhost:5000/api/animals", {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token")
          }
        });

        const data = await res.json();
        setAnimals(Array.isArray(data) ? data : []);

      } catch (err) {
        console.error(err);
      }
    };

    fetchAnimals();
  }, []);

  const addAnimal = async (e) => {
    e.preventDefault();

    const form = e.target;

    const newAnimal = {
      id: form[0].value,
      breed: form[1].value,
      age: form[2].value,
      gender: form[3].value,
      cost: form[4].value,
      health: form[5].value
    };

    await fetch("http://localhost:5000/api/animals", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + localStorage.getItem("token")
      },
      body: JSON.stringify(newAnimal)
    });

    const res = await fetch("http://localhost:5000/api/animals", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token")
      }
    });

    const data = await res.json();
    setAnimals(Array.isArray(data) ? data : []);

    form.reset();
  };

  const deleteAnimal = async (id) => {

    await fetch(`http://localhost:5000/api/animals/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token")
      }
    });

    setAnimals(animals.filter(a => a._id !== id));
  };

  return (
    <div className="container">

      <h2>{t.animalManagement}</h2>

      <input
        placeholder={t.searchAnimal}
        onChange={(e)=>setSearch(e.target.value)}
        style={{marginBottom:"10px"}}
      />

      <form className="form-grid" onSubmit={addAnimal}>
        <input placeholder={t.animalId} required />
        <input placeholder={t.breed} required />
        <input placeholder={t.age} required />
        <input placeholder={t.gender} required />
        <input placeholder={t.cost} required />
        <input placeholder={t.health} required />
        <button type="submit">{t.addAnimal}</button>
      </form>
      <div className="table-wrapper">
      <table className="styled-table">
        <thead>
          <tr>
            <th>{t.id}</th>
            <th>{t.breed}</th>
            <th>{t.age}</th>
            <th>{t.gender}</th>
            <th>{t.cost}</th>
            <th>{t.health}</th>
            <th>{t.action}</th>
          </tr>
        </thead>

        <tbody>

          {(Array.isArray(animals) ? animals : [])
            .filter(a => (a.id || "").includes(search))
            .map((a,index)=>(
              <tr key={index} style={{color:"black",background:"lightgray"}}>
                <td>{a.id}</td>
                <td>{a.breed}</td>
                <td>{a.age}</td>
                <td>{a.gender}</td>
                <td>₹ {a.cost}</td>
                <td>{a.health}</td>

                <td>
                  <button
                    onClick={()=>deleteAnimal(a._id)}
                    style={{
                      background:"red",
                      color:"white",
                      border:"none",
                      padding:"5px 10px",
                      cursor:"pointer",
                      borderRadius:"5px"
                    }}
                  >
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