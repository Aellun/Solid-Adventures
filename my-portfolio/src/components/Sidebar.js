// src/components/Sidebar.js
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faCode, faFileAlt, faTools, faEnvelope } from '@fortawesome/free-solid-svg-icons';
import './Sidebar.css';

const Sidebar = ({ setActiveComponent }) => {
    const menuItems = [
        { key: 'AboutMe', label: 'About Me', icon: faUser },
        { key: 'Projects', label: 'Projects', icon: faCode },
        { key: 'Resume', label: 'Resume', icon: faFileAlt },
        { key: 'Skills', label: 'Skills', icon: faTools },
        { key: 'Contact', label: 'Contact', icon: faEnvelope },
    ];

    return (
        <div className="sidebar">
            {/* Header Information at the Top */}
            <div className="header-info">
                <h2>OKELLO KEVIN</h2>
                <p>Software Engineer Student</p>
                <h5>At Hoberton School/ALX_Africa</h5>
            </div>

            {/* Menu Items */}
            <ul>
                {menuItems.map((item) => (
                    <li key={item.key} onClick={() => setActiveComponent(item.key)}>
                        <FontAwesomeIcon icon={item.icon} className="icon" />
                        {item.label}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Sidebar;
