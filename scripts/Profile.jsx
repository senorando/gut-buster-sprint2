import React, {useState,useEffect} from 'react';

import { ProfileCont } from './ProfileCont';
import { UserForm } from './userForm';
import { Login, Logout } from './GoogleButton';
import { Socket } from './Socket';

export function Profile(props) {
    const currentUser = props.currentUser;
    const isLoggingIn = props.isLoggingIn;
    const profileDetail = props.profileDetail;
    
    console.log(isLoggingIn);
    
    return (
        <div id = 'Profile'>
            { isLoggingIn?
                <div id = 'UserForm'>
                    <UserForm />
                </div>
                :
                <div id = 'ProfileContent'>
                    <ProfileCont currentUser = { currentUser } profileDetail = { profileDetail }/>
                    { currentUser.isLoggedIn?
                      <Logout />
                      :
                      <Login />
                    }
                </div>
            }
        </div>
        );
}