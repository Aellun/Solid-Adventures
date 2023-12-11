// src/components/Skills.js
import React from 'react';
import './Skills.css';

const Skills = () => {
    return (
        <div className="container-content">
            <h2>Skills</h2>
            <ul className="skills-list">
                <li>
                    <span className="skill-name">Python</span>
                    <p className="sub-note">Dynamic Libraries: Tkinter.</p>
                    <p className="sub-note">Object-Oriented Programming (OOP).</p>
                    <p className="sub-note">Data Structures and Collections.</p>
                </li>
                <li>
                    <span className="skill-name">HTML/5 CSS</span>
                    <p className="sub-note">Web Development Fundamentals.</p>
                    <p className="sub-note">CSS Styling and Frameworks.</p>
                </li>
                <li>
                    <span className="skill-name">C</span>
                    <p className="sub-note">Pointer and Memory Management</p>
                    <p className="sub-note">Data Structures.</p>
                </li>

                <li>
                    <span className="skill-name">React and Node.js</span>
                    <p className="sub-note">Front-End Development with React.</p>
                    <p className="sub-note">Back-End Development with Node.js.</p>
                </li>
                <li>
                    <span className="skill-name">Bash/Shell Scripting</span>
                    <p className="sub-note">Automation Solutions</p>
                    <p className="sub-note"> System Administration</p>
                    <p className="sub-note">Workflow Optimization:</p>
                </li>
                <li>
                    <span className="skill-name">Networking</span>
                    <p className="sub-note">Network Infrastructure Management.</p>
                    <p className="sub-note">Network Troubleshooting and Maintenance.</p>
                </li>
                <li>
                    <span className="skill-name">Database Management</span>
                    <p className="sub-note">Database Administration.</p>
                    <p className="sub-note"> Data Security and Integrity.</p>
                    <p className="sub-note"> Database Design and Implementation.</p>
                </li>
                <li>
                    <span className="skill-name">Remote Desktop Tools</span>
                    <p className="sub-note">Remote Desktop Administration.</p>
                    <p className="sub-note">Troubleshooting and Support.</p>
                    <p className="sub-note">Security and Access Control.</p>
                </li>
                {/* Add more skills with sub-notes as needed */}
            </ul>
        </div>
    );
};

export default Skills;
