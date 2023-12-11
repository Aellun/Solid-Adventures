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
                <img
                    src="/allan.jpg"
                    alt=''
                    height="200"
                    className="profile-image"
                />
                <h2>OKELLO KEVIN</h2>
                <h3>Software Engineer Student</h3>
                <h4>At Hoberton School/ALX_Africa</h4>
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
