// src/components/MainContent.js
import React from 'react';
import './MainContent.css';
import AboutMe from './AboutMe';
import Projects from './Projects';
import Contact from './Contact';
import Resume from './Resume';
import Skills from './Skills';
import CopyrightFooter from './CopyrightFooter';

const MainContent = ({ activeComponent }) => {
    const components = {
        AboutMe: <AboutMe />,
        Projects: <Projects />,
        Contact: <Contact />,
        Resume: <Resume />,
        Skills: <Skills />,
        CopyrightFooter: <CopyrightFooter />,
    };

    return <div className="main-content">{components[activeComponent]}</div>;
};

export default MainContent;
