// App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import OverviewPage from "./pages/OverviewPage";
import GameStartPage from "./pages/GameStartPage"; 

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/overview" element={<OverviewPage />} />
        <Route path="/game" element={<GameStartPage />} />
      </Routes>
    </Router>
  );
}

export default App;
