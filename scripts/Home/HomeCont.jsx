import React, { useState } from "react";

import { UserForm } from "../UserForm";
import { Chat } from '../Chat/Chat';

export function HomeCont(props) {
  const currentUser = props.currentUser;
  const isLoggingIn = props.isLoggingIn;

  return (
    <div>
      <div id = 'HomeContent'>
        { isLoggingIn?
          <UserForm />
          :
          <div className = 'Home'>
            <h3>Welcome { currentUser.name }</h3>
            <p>
                We aim to provide healthy food instructions,<br></br>
                diet plans and deliver a live chat accessible from the browser.<br></br>
                The  web app will provide a social login to allow users to easily identify themselves,<br></br>
                and feature a Comment/Discussion attitude, through that people can communicate with each other .
            </p>
          </div>
        }
        <Chat currentUser = { currentUser }/>
      </div>
      <div className = 'background'>
        <img src={'../static/GB.jpg'} alt="Logo" 
          style={{position: 'relative', left: 350, justify: 'contain'}}
        />
      </div>
    </div>
    );
}
