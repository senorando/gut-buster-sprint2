import React, { useState } from "react";

import { Socket } from './Socket';
import { Login, Logout } from './GoogleButton';
import { UserForm } from "./userForm";
import { HomeCont } from './HomeCont';

export function Home(props) {
  const currentUser = props.currentUser;
  const isLoggedIn = props.currentUser.isLoggedIn;
  
  const [isLoggingIn, setStatus] = useState(false);
  
  Socket.on('is logging in', (data) => {
    console.log(data);
    setStatus((prevStatus) => true);
  });
  Socket.off('is logging in', '');
  Socket.on('is not logging in', (data) => {
    setStatus((prevStatus) => false);
  });
  Socket.off('is not logging in', '');
  
  return (
    <div id = 'Home'>
        { isLoggingIn?
            <div id = 'UserForm'>
                <UserForm />
            </div>
            :
            <div id = 'HomeContent'>
                <HomeCont currentUser = { currentUser } />
                { isLoggedIn?
                  <Logout />
                  :
                  <Login />
                }
            </div>
        }
    </div>
    );
}
    
