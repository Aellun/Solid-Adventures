// src/App.js
import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import MainContent from './components/MainContent';
import "./App.css";

const App = () => {
  const [activeComponent, setActiveComponent] = useState('AboutMe');

  return (
    <div className="app">
      <Sidebar setActiveComponent={setActiveComponent} />
      <MainContent activeComponent={activeComponent} />
    </div>
  );
};

export default App;
