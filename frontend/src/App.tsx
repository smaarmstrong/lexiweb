import React from 'react';
import './App.css';
import Header from './components/Header/Header';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        {/* Your main content will go here */}
        <h1>Welcome to LexiWeb</h1>
        <p>Start managing your texts!</p>
      </main>
    </div>
  );
}

export default App;
