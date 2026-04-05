import React, { useState, useEffect, useRef } from "react";

export default function Profile({ logout }) {

  const [image, setImage] = useState("");
  const [open, setOpen] = useState(false);
  const [user, setUser] = useState("");
  const [loading, setLoading] = useState(true);

  const dropdownRef = useRef();

  // ✅ FETCH USER FROM BACKEND (WITH LOADING)
  useEffect(() => {
    const fetchUser = async () => {
      try {
        const res = await fetch("http://localhost:5000/api/users/profile", {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token")
          }
        });

        const data = await res.json();

        if (res.ok) {
          setUser(data.name);
          if (data.image) setImage(data.image);
        }

      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false); // ✅ stop loading
      }
    };

    fetchUser();
  }, []);

  // ✅ CLOSE DROPDOWN ON OUTSIDE CLICK
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
        setOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  // ✅ UPLOAD IMAGE
  const handleImageChange = async (e) => {
    const file = e.target.files[0];

    if (!file) return;

    if (file.size > 2 * 1024 * 1024) {
      alert("Image size should be less than 2MB");
      return;
    }

    const reader = new FileReader();

    reader.onloadend = async () => {
      const base64Image = reader.result;

      setImage(base64Image); // instant preview

      try {
        const res = await fetch("http://localhost:5000/api/users/upload", {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
            Authorization: "Bearer " + localStorage.getItem("token")
          },
          body: JSON.stringify({ image: base64Image })
        });

        if (!res.ok) {
          alert("Upload failed");
        }

      } catch (err) {
        console.error(err);
      }
    };

    reader.readAsDataURL(file);
  };

  return (
    <div className="topbar" style={{ position: "relative" }} ref={dropdownRef}>

      {/* ✅ LOADING PLACEHOLDER */}
      {loading ? (
        <div style={{
          width: "40px",
          height: "40px",
          borderRadius: "50%",
          background: "#ccc"
        }} />
      ) : (
        <img
          src={image || "https://via.placeholder.com/40"}
          alt="profile"
          onClick={() => setOpen(!open)}
          style={{
            width: "40px",
            height: "40px",
            borderRadius: "50%",
            cursor: "pointer",
            objectFit: "cover"
          }}
        />
      )}

      {open && (
        <div style={{
          position: "absolute",
          top: "50px",
          right: "0",
          background: "lightgray",
          color: "black",
          border: "1px solid #ccc",
          borderRadius: "8px",
          padding: "10px",
          width: "160px",
          zIndex: 999
        }}>

          <p style={{ fontWeight: "bold" }}>
            {user || "Farmer"}
          </p>

          <hr />

          <label style={{ cursor: "pointer" }}>
            Upload Photo
            <input
              type="file"
              accept="image/*"
              onChange={handleImageChange}
              style={{ display: "none" }}
            />
          </label>

          <hr />

          <p style={{ cursor: "pointer" }}>Profile</p>

          <p 
            style={{ cursor: "pointer", color: "red" }} 
            onClick={logout}
          >
            Logout
          </p>

        </div>
      )}
    </div>
  );
}