import React, { useState } from "react";

import { Socket } from './Socket';
import { UserForm } from "./userForm";
import { HomeCont } from './HomeCont';

export function Home(props) {
  const currentUser = props.currentUser;
  const isLoggedIn = props.currentUser.isLoggedIn;
  const isLoggingIn = props.isLoggingIn;
  console.log(props);
  return (
    <div id = 'Home'>
        { isLoggingIn?
            <div id = 'UserForm'>
                <UserForm />
            </div>
            :
            <div id = 'HomeContent'>
                <HomeCont currentUser = { currentUser } />
            </div>
        }
    </div>
    );
}
    
