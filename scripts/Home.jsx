import React, { useState } from "react";

import { Socket } from './Socket';
import { Login, Logout } from './GoogleButton';
import { UserForm } from "./userForm";
import { HomeCont } from './HomeCont';

export function Home() {
  const [currentUser, setUser] = useState({
      name: '', email: '', sid: ''
  });
  const [isLoggingIn, setStatus] = useState(false);
  const [isLoggedIn, setLogin] = useState(false);
  console.log('Login status: ' + isLoggedIn);
  
  Socket.on('success login', (data) => {
      if (data.sid === Socket.id) {
          setUser((prevState) => ({
            name: data.name,
            email: data.email,
            sid: data.sid,
          }));
          setLogin((prevLogin) => true);
          setStatus((prevStatus) => false);
        }
  });
  Socket.off('success login', '');
  Socket.on('is logging in', (data) => {
    console.log(data);
    setStatus((prevStatus) => true);
  });
  Socket.off('is logging in', '');
  
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
    
