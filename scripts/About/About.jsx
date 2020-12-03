import * as React from 'react';

export function About() {
    
    return (
        <div id = 'About'>
            <div className = 'a1'>
                <p>
                  We aim to provide healthy food instructions, diet plans and deliver a live chat accessible from the browser.
                  The web app will provide a social login to allow users to easily identify themselves, and feature a live chat, through that people can communicate with each other.<br/>
                </p>
            </div>
            <div className = 'a2'>
                <h1>Team Members</h1>
                <div className = 'team-intro'>
                    <div className = 'team-member'>
                        <h4>Andy Martinez</h4>
                        <p>
                            Hello, I'm Oreoluwa Akeredolu. I'm a current student at NJIT persuing a degree in Computer Science.
                            I enjoy the process of problem solving, which has lead me down the path to absolutely adoring
                            all aspects of the software development process.  Working on this project has absolutely
                            exposed me to learning new technoloiges and how it is to truly work in a team enviroment.<br/>
                            I'm glad to be working with such an awesome team.
                        </p>
                    </div>
                    <div className = 'team-member'>
                        <h4>Oreoluwa Akeredolu</h4>
                        <p>
                            Hello, I'm Oreoluwa Akeredolu. I'm a current student at NJIT persuing a degree in Computer Science.
                            I enjoy the process of problem solving, which has lead me down the path to absolutely adoring
                            all aspects of the software development process.  Working on this project has absolutely
                            exposed me to learning new technoloiges and how it is to truly work in a team enviroment.<br/>
                            I'm glad to be working with such an awesome team.
                        </p>
                    </div>
                    <div className = 'team-member'>
                        <h4>Jinal patel</h4>
                        <p>
                            Hello, I'm Oreoluwa Akeredolu. I'm a current student at NJIT persuing a degree in Computer Science.
                            I enjoy the process of problem solving, which has lead me down the path to absolutely adoring
                            all aspects of the software development process.  Working on this project has absolutely
                            exposed me to learning new technoloiges and how it is to truly work in a team enviroment.<br/>
                            I'm glad to be working with such an awesome team.
                        </p>
                    </div>
                    <div className = 'team-member'>
                        <h4>Nisrag Patel</h4>
                        <p>
                            Hello, I'm Oreoluwa Akeredolu. I'm a current student at NJIT persuing a degree in Computer Science.
                            I enjoy the process of problem solving, which has lead me down the path to absolutely adoring
                            all aspects of the software development process.  Working on this project has absolutely
                            exposed me to learning new technoloiges and how it is to truly work in a team enviroment.<br/>
                            I'm glad to be working with such an awesome team.
                        </p>
                    </div>
                </div>
            </div>
            <div className = "a3">
                <h1>Technologies</h1>
                <div className="technologies">
                    <ul className="technologies-list">
                        <li><a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">Python Flask</a></li>
                    </ul>
                    <ul className="technologies-list">
                        <li><a href="https://reactjs.org/" target="_blank">React.js</a></li>
                    </ul>
                    <ul className="technologies-list">
                        <li><a href="https://www.postgresql.org/" target="_blank">Postgresql</a></li>
                    </ul>
                    <ul className="technologies-list">
                        <li><a href="https://www.heroku.com/" target="_blank">Heroku</a></li>
                    </ul>
                    <ul className="technologies-list">
                        <li><a href="https://circleci.com/" target="_blank">Circle CI</a></li>
                    </ul>
                </div>
            </div>
        </div>
    );
}