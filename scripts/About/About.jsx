import * as React from 'react';

export function About() {
    
    return (
        <div id = 'About'>
            <div className = 'a1'>
                <h1>Who We Are?</h1>
                <p>
                We aim to provide healthy food options, meal plans, workout plans, and also deliver a live chat feature accessible from the browser.
                This web app provides a secure Google login that allows users to identify themselves, a custom statistical profile for body macros,
                workouts, and a food search tool that shows a meal, its calorie count, preparation time and a link to the recepie. 
                This app also features a  live chat platform through which users can communicate with each other.<br/>
                </p>
            </div>
            <div className = 'a2'>
                <h1>Team Members</h1>
                <div className = 'team-intro'>
                    <div className = 'team-member'>
                        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
                        <img src="./static/Andy.png" class="member-picture"/>
                        <h4>Andy Martinez</h4>
                        <a href="https://github.com/senorando" target="_blank" class="git-logo"><i className="fa fa-github" ></i></a>
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
                        <a href="https://github.com/atorisemofe" target="_blank"><i className="fa fa-github" ></i></a>
                        <p>
                            Hello, I'm Oreoluwa Akeredolu. I'm a current student at NJIT persuing a degree in Computer Science.
                            I enjoy the process of problem solving, which has lead me down the path to absolutely adoring
                            all aspects of the software development process.  Working on this project has absolutely
                            exposed me to learning new technoloiges and how it is to truly work in a team enviroment.
                            I'm glad to be working with such an awesome team.
                        </p>
                    </div>
                    <div className = 'team-member'>
                        <img src="./static/Jinal.png" class="member-picture"/>
                        <h4>Jinal patel</h4>
                        <a href="https://github.com/jsp88" target="_blank"><i className="fa fa-github" ></i></a>
                        <p>
                            Hello, I'm Jinal Patel. I'm a current student at NJIT pursuing a degree in Computer Science. 
                            I'm extremely eager to introduce our site that me and my team member has been dealing with.
                            I enjoyed working on the frontend development part of this project and gained knowlage in the backend development while learning new technologies.
                            This was a perfect opportunity to demostrate valueable skills such as team collaboration and leadership.
                        </p>
                    </div>
                    <div className = 'team-member'>
                        <img src="./static/Nisrag.png" class="member-picture"/>
                        <h4>Nisrag Patel</h4>
                        <a href="https://github.com/np575" target="_blank"><i className="fa fa-github" ></i></a>
                        <a href="https://www.linkedin.com/in/nisarg-patel-/" target="_blank"><i className="fa fa-linkedin" ></i></a>
                        <p>
                            Hello, I'm Nisarg Patel. I'm a rising senior at NJIT persuing a degree in Computer Science.
                            I enjoy working on the team enviroment while showcasing my skills and learning form others.
                            I implemented most of the logic in the backend code and handled front-end functionalities in the project.  
                            Building this project, collaborating with the team and an industrial mentor who taught me various new technologies
                            and how they work has been a wonderful experience.
                            I now look forward to improving my skills and practice in fullstack development.<br/>
                        </p>
                    </div>
                </div>
            </div>
            <div className = "a4">
                <h1>Frequently Asked Questions</h1>
                <div class="container">
                <div class="box box-1">
                    <h2>How did we make Gut Buster?</h2>
                    <p>
                    A list of the most notable technologies used in this web-app are included at the bottom of this page.<br/><br/>
                    For the backend, the main programming language we used was Python. With Python, we utilized the Flask Micro-Framework 
                    to serve web pages. Along with this, we used socket.io to interface between the front-end and the back-end. Persistence 
                    was achieved using Postgresql and SQLAlchemy to provide an easy interface to interact with the database via Python.<br/><br/>
                    Comments are stored in the database, as well as future user information and preferences. For the front-end, the main technology that 
                    we used was functional React.js, as well as some vanilla HTML, CSS, and Javascript. A number of different packages were
                    utilized with React as well, which can be found on the Github page.<br/><br/>
                    Collaboration was utilized using Git and Github. Final deployment of this web app was done on Heroku.
                    </p>
                </div>
                
                <div class="box box-2">
                    <h2>Why did we create Gut Buster?</h2>
                    <p>
                    A list of the most notable technologies used in this web-app are included at the bottom of this page. 
                    For the backend, the main programming language we used was Python. With Python, we utilized the Flask Micro-Framework 
                    to serve web pages. Along with this, we used socket.io to interface between the front-end and the back-end. Persistence 
                    was achieved using Postgresql and SQLAlchemy to provide an easy interface to interact with the database via Python. Comments
                    are stored in the database, as well as future user information and preferences. For the front-end, the main technology that 
                    we used was functional React.js, as well as some vanilla HTML, CSS, and Javascript. A number of different packages were
                    utilized with React as well, which can be found on the Github page. Collaboration was utilized using Git and Github. Final
                    deployment of this web app was done on Heroku.
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