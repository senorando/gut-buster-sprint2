import React, {useState,useEffect} from 'react';

import { ProfileCont } from './ProfileCont';

import { Socket } from '../Socket';

export function Profile(props) {
    const currentUser = props.currentUser;
    const isLoggingIn = props.isLoggingIn;
    const profileDetail = props.profileDetail;
    const userWeight = props.userWeight;
    
    return (
        <div id = 'Profile'>
            { currentUser.isLoggedIn?
                <ProfileCont currentUser = { currentUser } 
                                profileDetail = { profileDetail }
                                userWeight = { userWeight }
                                date = {props.date}
                                isLoggingIn = { isLoggingIn } />
                :
                <ProfileCont currentUser = { currentUser } 
                                profileDetail = { profileDetail }
                                userWeight = { userWeight }
                                date = {props.date}
                                isLoggingIn = { isLoggingIn } />
            }
        </div>
        );
}