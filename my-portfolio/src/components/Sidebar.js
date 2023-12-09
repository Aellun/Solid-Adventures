// src/components/Sidebar.js
import React from 'react';
import './Sidebar.css';

const Sidebar = ({ setActiveComponent }) => {
    const menuItems = ['AboutMe', 'Projects', 'Resume', 'Skills', 'Contact'];

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
                    <li key={item} onClick={() => setActiveComponent(item)}>
                        {item}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Sidebar;
