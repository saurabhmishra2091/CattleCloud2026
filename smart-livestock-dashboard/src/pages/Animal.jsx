import React, { useState, useEffect } from "react";

export default function Animal() {

  const [animals, setAnimals] = useState([]);
  const [search, setSearch] = useState("");

  // ✅ FETCH WITH TOKEN + SAFE
  useEffect(() => {
    const fetchAnimals = async () => {
      try {
        const res = await fetch("http://localhost:5000/api/animals", {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token")
          }
        });

        const data = await res.json();

        // ✅ IMPORTANT FIX
        setAnimals(Array.isArray(data) ? data : []);

      } catch (err) {
        console.error(err);
      }
    };

    fetchAnimals();
  }, []);

  // ✅ ADD ANIMAL
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

    // refresh
    const res = await fetch("http://localhost:5000/api/animals", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token")
      }
    });

    const data = await res.json();
    setAnimals(Array.isArray(data) ? data : []);

    form.reset();
  };

  // ✅ DELETE
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

      <h2>🐄 Animal Management</h2>

      <input
        placeholder="Search Animal ID"
        onChange={(e)=>setSearch(e.target.value)}
        style={{marginBottom:"10px"}}
      />

      <form className="form-grid" onSubmit={addAnimal}>
        <input placeholder="Animal ID" required />
        <input placeholder="Breed" required />
        <input placeholder="Age" required />
        <input placeholder="Gender" required />
        <input placeholder="Purchase Cost" required />
        <input placeholder="Health Status" required />
        <button type="submit">Add Animal</button>
      </form>

      <table className="styled-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Breed</th>
            <th>Age</th>
            <th>Gender</th>
            <th>Cost</th>
            <th>Health</th>
            <th>Action</th>
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