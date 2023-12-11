// src/components/Projects.js
import React from 'react';
import './Projects.css';
const Projects = () => {
    return (
        <div className="container-content">
            <h1>PROJECTS</h1>
            <div>
                <h3><a href="https://github.com/Aellun/Solid-Adventures/tree/main/task-manager_GUI" target="_blank">Task Manager</a></h3>
                <p>Description:<br />
                    Built with Python and Tkinter library and SQLite3<br />
                    This an application that enable you organise your to do list
                    for the specified period you decide.</p>

            </div>
            <div>
                <h3><a href="https://github.com/Aellun/Solid-Adventures/tree/main/Password_generator" target="_blank">Password Genrator</a></h3>
                <p>Description:<br />
                    Built with Python and Tkinter<br />
                    This is a destop application you can use to
                    generate, store and manage secure random Password
                </p>
            </div>
            <div>
                <h3><a href="https://github.com/Aellun/Solid-Adventures/tree/main/mycommand-console" target="_blank">Console</a></h3>
                <p>Description:<br />
                    Built with Python<br />
                    This is console that mimics the functionality of terminal in Linux or CMD in Windows
                    The commands for both windows are fused together, meaning Window and Linux users can
                    use it easily with the same command.</p>
            </div>
            <div>
                <h3><a href="https://github.com/Aellun/Solid-Adventures/tree/main/calculator" target="_blank">Calculator</a></h3>
                <p>Description:<br />
                    Built with Python Tkinter Library<br />
                    This is just a simple calculator which the user can download and use on the desktop
                    for those who can not the pyinstaller it has an executable  which you can download and start using
                    immediately</p>
            </div>
            <div>
                <h3><a href="https://github.com/Aellun/Solid-Adventures/tree/main/my-portfolio" target="_blank">Portfolio</a></h3>
                <p>Description:<br />
                    Built with Javascript,React,css<br />
                    Simpke web- based application that display my skills</p>
            </div>
            <h3><a href='https://github.com/Aellun/Solid-Adventures/tree/main/app_logging' target='_blank'>Logs</a></h3>
            <p>Description:<br />
                built with Python Tkinter library and SQLite3<br />
                This is graphical user interface PC logs that stores the all the application and servises
                running in the host pc as long as it is set to run. user can review and analyze such logs easilyby choosing the
                the dates</p>
        </div>

    );
};

export default Projects;
