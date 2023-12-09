// src/App.js
import React, { useState } from 'react';
import './App.css';
import Skills from './components/Skills';
import AboutMe from './components/AboutMe';
import Projects from './components/Projects';
import Contact from './components/Contact';
import Resume from './components/Resume';
import Sidebar from './components/Sidebar';
import MainContent from './components/MainContent';
import CopyrightFooter from './components/CopyrightFooter';

function App() {
  const [activeComponent, setActiveComponent] = useState('Header');

  return (
    <div className="app">
      <Sidebar setActiveComponent={setActiveComponent} />
      <MainContent activeComponent={activeComponent} />
    </div>
  );
}

export default App;
