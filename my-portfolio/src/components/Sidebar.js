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
                <h1>Okello Kevin</h1>
                <p>Full-Stack Software Engineer</p>
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
