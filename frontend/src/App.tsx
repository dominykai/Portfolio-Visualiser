import './App.css'
import { Routes, Route } from "react-router-dom";
import SignUpPage from "@/pages/authorisation/signup-page.tsx";
import LoginPage from "@/pages/authorisation/login-page.tsx";
import RootPage from "@/pages/root.tsx";

function App() {
  return (
    <Routes>
      {/* */}
      <Route path="/" element={<RootPage />} />

      {/* Authorisation Paths */}
      <Route path="/signup" element={<SignUpPage />} />
      <Route path="/login" element={<LoginPage />} />
    </Routes>
  )
}

export default App
