import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";
import { useEffect, useState } from "react";

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

export default function FarmerDashboard() {

  const [animals, setAnimals] = useState([]);
  const [milkRecords, setMilkRecords] = useState([]);
  const [vaccines, setVaccines] = useState([]);

  // ✅ FETCH WITH TOKEN + SAFE DATA
  useEffect(() => {

    const fetchData = async () => {
      try {
        const token = localStorage.getItem("token");

        // 🐄 Animals
        const animalRes = await fetch("http://localhost:5000/api/animals", {
          headers: {
            Authorization: "Bearer " + token
          }
        });
        const animalData = await animalRes.json();
        setAnimals(Array.isArray(animalData) ? animalData : []);

        // 🥛 Milk
        const milkRes = await fetch("http://localhost:5000/api/milk", {
          headers: {
            Authorization: "Bearer " + token
          }
        });
        const milkData = await milkRes.json();
        setMilkRecords(Array.isArray(milkData) ? milkData : []);

        // 💉 Vaccines (if backend ready)
        setVaccines([]);

      } catch (err) {
        console.error(err);
      }
    };

    fetchData();
  }, []);

  const today = new Date().toISOString().split("T")[0];

  const totalAnimals = animals.length;

  // ✅ SAFE FILTER
  const todayMilk = (Array.isArray(milkRecords) ? milkRecords : [])
    .filter(m => m.date === today)
    .reduce((sum, m) => sum + Number(m.quantity), 0);

  const milkPrice = 70;
  const revenueToday = todayMilk * milkPrice;

  const upcomingVaccines = vaccines.length;

  const healthAlerts = vaccines;

  // ✅ SAFE REDUCE
  const totalMilk = (Array.isArray(milkRecords) ? milkRecords : [])
    .reduce((sum, r) => sum + Number(r.quantity), 0);

  const animalMilk = {};

  (Array.isArray(milkRecords) ? milkRecords : []).forEach(r => {
    if (!animalMilk[r.animalId]) {
      animalMilk[r.animalId] = 0;
    }
    animalMilk[r.animalId] += Number(r.quantity);
  });

  const topAnimal =
    Object.entries(animalMilk).sort((a, b) => b[1] - a[1])[0];

  const performanceScore =
    (totalMilk * 0.5) +
    (totalAnimals * 2) +
    (revenueToday * 0.1);

  const days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];
  const weeklyData = new Array(7).fill(0);

  (Array.isArray(milkRecords) ? milkRecords : []).forEach(r => {
    const d = new Date(r.date).getDay();
    const index = d === 0 ? 6 : d - 1;
    weeklyData[index] += Number(r.quantity);
  });

  const data = {
    labels: days,
    datasets: [
      {
        label: "Milk Production (Liters)",
        data: weeklyData,
        backgroundColor: "#2e7d32",
        borderRadius: 8,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
    },
  };

  return (
    <div style={styles.container}>

      <div style={styles.welcome}>
        <h2>Welcome, {localStorage.getItem("user") || "Farmer"} 👋</h2>
        <p>{new Date().toDateString()}</p>
      </div>

      <div style={styles.grid}>

        <Card title="🐄 Total Animals" value={totalAnimals} color="#e8f5e9" />
        <Card title="💉 Upcoming Vaccines" value={upcomingVaccines} color="#fff3e0" />
        <Card title="🥛 Today Milk" value={`${todayMilk} L`} color="#e3f2fd" />
        <Card title="💰 Revenue Today" value={`₹${revenueToday}`} color="#f3e5f5" />
        <Card title="⚠️ Health Alerts" value={healthAlerts.length} color="#ffe5e5" />
        <Card title="🥛 Total Milk" value={`${totalMilk} L`} color="#e8f5e9" />
        <Card title="🏆 Top Animal" value={topAnimal ? topAnimal[0] : "N/A"} color="#fff3e0" />
        <Card title="⭐ Farm Score" value={Math.round(performanceScore)} color="#f3e5f5" />

      </div>

      <div style={styles.chartCard}>
        <h3>Weekly Milk Production</h3>
        <Bar data={data} options={options} />
      </div>

    </div>
  );
}

function Card({title,value,color}){
  return(
    <div style={{...styles.card, background:color}}>
      <h3>{title}</h3>
      <p style={styles.number}>{value}</p>
    </div>
  )
}

const styles = {
  container:{ padding:"25px", minHeight:"100vh" },
  welcome:{ marginBottom:"20px" },
  grid:{
    display:"grid",
    gridTemplateColumns:"repeat(auto-fit,minmax(200px,1fr))",
    gap:"20px",
    marginBottom:"30px"
  },
  card:{
    padding:"20px",
    borderRadius:"12px",
    boxShadow:"0 4px 10px rgba(0,0,0,0.1)",
    textAlign:"center",
    color:"black"
  },
  number:{ fontSize:"28px", fontWeight:"bold", marginTop:"10px" },
  chartCard:{
    background:"white",
    padding:"25px",
    borderRadius:"12px",
    boxShadow:"0 4px 10px rgba(0,0,0,0.1)"
  }
};