import React from "react";
import { Login } from "./GoogleButton";

export function Home() {
  return (
    <div>
        <div> Gut Buster </div>
        <div>
            <h3>Welcome to the Gut Buster </h3>
            <p>
                We aim to provide healthy food instructions,<br></br>
                diet plans and deliver a live chat accessible from the browser.<br></br>
                The  web app will provide a social login to allow users to easily identify themselves,<br></br>
                and feature a Comment/Discussion attitude, through that people can communicate with each other .
            </p>
        </div>
        <div>
            <h1>Login with Google OAuth!</h1>
        </div>
        <div>
            <Login />
        </div>
       </div>
    );
}
    
