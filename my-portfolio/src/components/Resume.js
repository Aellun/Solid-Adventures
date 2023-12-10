// src/components/Resume.js
import React from 'react';
import './Resume.css';
const Resume = () => {
    return (
        <div className="resume-container">
            <h2>Projects</h2>
            <div>
                <h3>Project 1</h3>
                <p>Description of Project 1.</p>
            </div>
            <div>
                <h3>Project 2</h3>
                <p>Description of Project 2.</p>
            </div>
            {/* Add more projects as needed */}
        </div>
    );
};

export default Resume;
