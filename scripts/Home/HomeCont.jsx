import React, { useState } from "react";

import { UserForm } from "../UserForm";
import { Chat } from '../Chat/Chat';

export function HomeCont(props) {
  const currentUser = props.currentUser;
  const isLoggingIn = props.isLoggingIn;

  return (
    <div id = 'HomeContent'>
      { isLoggingIn?
        <UserForm />
        :
        <div className = 'Home'>
          { currentUser.isLoggedIn?
            <h3>Welcome { currentUser.name }</h3>              
            :
            <h3>Welcome! Please login to use Gut Buster</h3>
          }
          <div>
            <ul>
              <li>Gut Buster is the world's leading fitness application!</li>
              <li>Once signed in you can view your profile, see your vitals and view recommendations made by our cutting edge software!</li>
              <li>You can interact with other active users in our live chat!</li>
            </ul>
          </div>
        </div>
      }
      <Chat currentUser = { currentUser }/>
    </div>
    );
}
