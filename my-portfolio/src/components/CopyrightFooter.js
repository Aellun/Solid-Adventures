// src/components/CopyrightFooter.js
import React, { useEffect } from 'react';
import './CopyrightFooter.css';

const CopyrightFooter = () => {
    useEffect(() => {
        console.log('CopyrightFooter mounted');
        return () => {
            console.log('CopyrightFooter unmounted');
        };
    }, []);

    return (
        <footer className="copyright-footer">
            <p>&copy; 2023 Okello. All rights reserved.</p>
        </footer>
    );
};

export default CopyrightFooter;
