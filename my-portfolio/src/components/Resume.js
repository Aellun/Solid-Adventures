// src/components/Resume.js
import React from 'react';
import './Resume.css';

const Resume = () => {
    return (
        <div className="container-content">
            <h1>RESUME</h1>
            <div>
                <h2>Professional Experience</h2>
                <h4>IT Support-Digitization --- <a href='https://disigroup.com/about-us/' target='_blank'>Digital Imaging and Scanning International</a></h4>
                <h4>Period --- October 2022- Present</h4>
                <h4>Responsibilities and Achievements:</h4>
                <p className="resume-paragraph">
                    Evaluate, install, and configure computer hardware components <br />
                    Troubleshoot and resolve hardware issues <br />
                    Network infrastructure setup and maintenance <br />
                    Install and configure software applications and licenses.<br />
                    Databases Setup, configuration, and troubleshooting.
                </p>
            </div>
            <div>
                <h4>Assistant Project Team Leader --- <a href='https://disigroup.com/about-us/' target='_blank'>Digital Imaging and Scanning International</a></h4>
                <h4>Period --- June 2021- September 2022</h4>
                <h4>Responsibilities and Achievements:</h4>
                <p className="resume-paragraph">
                    Managed and led a team of 10 supervisors and over 100 digitization clerks <br />
                    Successfully manage and lead a digitization team by setting clear goals, assigning tasks, and providing constructive feedback, fostering a productive work environment. <br />
                    Develop and implement digitization processes and procedures that align with industry standards, ensuring compliance and optimizing efficiency.<br />
                    Coordinate seamlessly with IT and other teams to establish and maintain digital systems and tools, fostering a collaborative working environment.<br />
                    Oversee the entire digitization process, monitoring progress, resolving issues promptly, and communicating effectively with stakeholders to keep projects on track.<br />
                    Ensure the digitization team has the necessary resources and equipment, while also providing comprehensive training and support to enhance the team's skills and knowledge for optimal performance.
                </p>
            </div>
            <div>
                <h4>Digitization Supervisor --- <a href='https://disigroup.com/about-us/' target='_blank'>Digital Imaging and Scanning International</a></h4>
                <h4>Period --- January 2020-May 2021</h4>
                <h4>Responsibilities and Achievements:</h4>
                <p className="resume-paragraph">
                    Managed and led a team of 10 supervisors and over 100 digitization clerks <br />
                    oversaw Preparation,scanning, Quality-Control, indexing, and cataloging digital images <br />
                    Monitored project progress, resolved issues, and communicated with Team Leader and stakeholders.<br />
                    Reviewed and analyzed data for quality and completeness. Implemented process improvements.<br />

                </p>
            </div>
            <div>
                <h4>Attachee-IT Technician --- <a href='https://kenya.ilu.edu/' target='_blank'>International Leadership University</a></h4>
                <h4>Period --- September 2018 - December 2018</h4>
                <h4>Responsibilities and Achievements:</h4>
                <p className="resume-paragraph">
                    Installed, configured, and maintained computer hardware and software systems. <br />
                    Troubleshoot and resolve technical issues for users <br />
                    Managed and maintained networks, servers, and other IT infrastructure.<br />
                    Provided training and support to users on new technology and software applications.<br />


                </p>
            </div>
            <div>
                <h2>Education</h2>
                <h4>Full Stack Software Engineering --- <a href="https://www.alxafrica.com/news/ali-acquires-holberton-school/" target="_blank"> Holberton School and ALX Africa</a></h4>
                <h4>Period --- May 2023 - May 2024</h4>
                <h4>Covered::</h4>
                <p className="resume-paragraph">
                    <strong>Version Control</strong>:Git <br />
                    <strong>Programming Languages:</strong> <br />
                    <em>C (Pointers, Arrays, Strings, Structures, Dynamic Libraries, Recursion, etc.) </em><br />
                    <em>Python (Fundamentals, Data Structures, Exceptions, Classes and Objects, Inheritance,Input/Output, and more)</em>.<br />
                    <strong>Shell Scripting:</strong><br />
                    Shell Basics, Permissions, I/O Redirections and Filters, Init Files, Variables, and Expansions
                </p>
            </div>
            <div>
                <h4>Bachelor of Technology(BIT) --- <a href='https://www.tukenya.ac.ke/sites/default/files/downloads/TUK-list-of-gruaduands-2018.pdf' target='_blank'>The Technical University of Kenya </a></h4>
                <h4>Period --- August 2014-December 2018</h4>
                <h5>Second Class Lower Division</h5>
                <h4>Covered:</h4>

                <p className="resume-paragraph">
                    System analysis and design <br />
                    Business process modelling and simulations <br />
                    Business information systems.<br />
                    Information system Audit.<br />
                    Information system Security.<br />
                    IT project management<br />
                    Databases Management system
                </p>
                <div>
                    <h2>Certifications</h2>
                    <h4>Electronic Document Management (ECM) --- <a href="https://hk.newgensoft.com/partners/#resellers" target="_blank"> NewgenSoft</a></h4>
                    <h4>Period --- November 2022</h4><br />

                    <h4>Leadership and Management (ECM) --- <a href="https://noblework.org/" target="_blank"> Noblework Foundation</a></h4>
                    <h4>Period --- July 2021</h4><br />

                    <h4> Fundamental of Digital Marketing--- <a href="https://skillshop.exceedlms.com/student/collection/648385-digital-marketing?locale=en" target="_blank"> Google Digital Skills</a></h4>
                    <h4>Period --- July 2021</h4><br />

                    <h4> Certificate In Information Technology--- <a href="https://www.google.com/search?sca_esv=589766361&sxsrf=AM9HkKn0uTHQS4wbzQM7CT1ZHNrQ66tBfA:1702297227629&q=Cathedral+Church+Of+Christ+The+King&ludocid=1352565100568654148&lsig=AB86z5XAf6Dv27egK50bp54u2Y90&sa=X&ved=2ahUKEwia87esr4eDAxXBe6QEHXZvCWIQ8G0oAHoECEwQAQ&biw=1850&bih=944&dpr=1" target="_blank"> Christ The King Training Institute Nakuru</a></h4>
                    <h4>Period --- July 2021</h4><br />
                </div>
            </div>

            {/* Add more projects as needed */}
        </div>
    );
};

export default Resume;
