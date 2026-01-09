import './App.css'
import { Routes, Route } from "react-router-dom";
import SignUpPage from "@/pages/signup.tsx";
import LoginPage from "@/pages/login.tsx";

function App() {
  return (
    <Routes>
      {/* Authorisation Paths */}
      <Route path="/signup" element={<SignUpPage />} />
      <Route path="/login" element={<LoginPage />} />
    </Routes>
  )
}

export default App
