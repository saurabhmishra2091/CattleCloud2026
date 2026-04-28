import { createContext, useState } from "react";

export const LanguageContext = createContext();

export function LanguageProvider({ children }) {

  const [lang, setLang] = useState(
    localStorage.getItem("lang") || "en"
  );

  const toggleLang = () => {
    const newLang = lang === "en" ? "hi" : "en";
    setLang(newLang);
    localStorage.setItem("lang", newLang);
  };

  return (
    <LanguageContext.Provider value={{ lang, toggleLang }}>
      {children}
    </LanguageContext.Provider>
  );
}