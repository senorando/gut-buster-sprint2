import React, {useState,useEffect} from 'react';

import { ProfileCont } from './ProfileCont';
import { UserForm } from '../userForm';
import { Socket } from '../Socket';

export function Profile(props) {
    const currentUser = props.currentUser;
    const isLoggingIn = props.isLoggingIn;
    const profileDetail = props.profileDetail;
    const userWeight = props.userWeight;
    
    return (
        <div id = 'Profile'>
            { isLoggingIn?
                <div id = 'UserForm'>
                    <UserForm />
                </div>
                :
                currentUser.isLoggedIn?
                    <div id = 'ProfileContent'>
                        <ProfileCont currentUser = { currentUser } 
                                        profileDetail = { profileDetail }
                                        userWeight = { userWeight }/>
                    </div>
                    :
                    <div id = 'ProfileContent'>
                        <h3>Please login with Google in order to see your profile</h3>
                    </div>
            }
        </div>
        );
}