
import * as React from 'react';
import { Login ,  Logout } from './GoogleButton';
import { Socket } from './Socket';
import { profileContent} from './profileContent';
import { foodSearchContent } from './foodSearchContent'; 

export function homeContent() {
    // TODO
    
    return (
    <body>
    <head>
        <title> Gut Buster </title>
    </head>
    <h1> Gut Buster </h1>
        <h2>
        <Button onClick={e => this.profileContent()}>View Profile</Button>
        <Button onClick={e => this.foodSearchContent()}>Food Search</Button>
        <Logout/> 
        </h2>
        <div>
            <h3>Wellcome to the Gut Buster </h3>
            <p>
                We aim to provide healthy food instructions,<br></br>
                diet plans and deliver a live chat accessible from the browser.<br></br>
                The  web app will provide a social login to allow users to easily identify themselves,<br></br>
                and feature a Comment/Discussion attitude, through that people can communicate with each other .
            </p>
        </div>
        <div>
            <h1>Login with Google OAuth!</h1>
            <Login/>
        </div>
        </body>
    );
}

    
    
