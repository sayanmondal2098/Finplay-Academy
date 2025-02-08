// src/pages/GamePage.js
import React from "react";
import "./GamePage.css"; // Import optional CSS for the GamePage

const GamePage = () => {
  return (
    <div className="game-page">
      <header className="game-header">
        <h1>Welcome to the Game Page!</h1>
      </header>
      <main className="game-content">
        <p>
          Get ready for an exciting journey to master financial literacy through
          interactive challenges and real-life scenarios.
        </p>
        {/* Additional game components and logic can be added here */}
      </main>
    </div>
  );
};

export default GamePage;
