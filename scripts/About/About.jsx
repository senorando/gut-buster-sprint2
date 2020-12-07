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
                        <img src="./static/Andy.png" class="member-picture"/>
                        <h4>Andy Martinez</h4>
                        <p>
                            Hi, I'm Andy! I came up with the idea of this app because as someone into fitness, 
                            I want to have a good fitness app that has all aspects combined into it, nutrition and exercise.
                            I handled a lot of the backend and frontend of the app and orchestrated the database persistence on the app. 
                            I also created the fitness API/database from scratch since we couldn't find an API online.
                            I've enjoyed making this app despite the difficulties it's had and I'm looking forward to more full stack development in the future!
                        </p>
                    </div>
                    <div className = 'team-member'>
                        <img src="./static/Oreo.png" class="member-picture"/>
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
                        <img src="./static/Nisrag.png" class="member-picture"/>
                        <h4>Nisrag Patel</h4>
                        <p>
                            Hello, I'm Nisarg Patel. I'm a rising senior at NJIT persuing a degree in Computer Science.
                            I enjoy working on the team enviroment while showcasing my skills and learning form others.
                            I implemented most of the logic in the backend code and handled front-end functionalities in the project.  
                            Building this project, collaborating with the team and an industrial mentor who taught me many technologies
                            and how they work has been a wonderful experience.<br/>
                            I now look forward to improving my skills and practice in fullstack development.<br/>
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