import React, {useState,useEffect} from 'react';

import { ProfileCont } from './ProfileCont';
import { UserForm } from '../UserForm';
import { Socket } from '../Socket';

export function Profile(props) {
    const currentUser = props.currentUser;
    const isLoggingIn = props.isLoggingIn;
    const profileDetail = props.profileDetail;
    const userWeight = props.userWeight;
    const date= props.date;
    return (
        <div id = 'Profile'>
            { isLoggingIn?
                <div id = 'UserForm'>
                    <UserForm />
                </div>
                :
                currentUser.isLoggedIn?
                    <ProfileCont currentUser = { currentUser } 
                                    profileDetail = { profileDetail }
                                    userWeight = { userWeight }
                                    date = {props.date}/>
                    :
                    <div id = 'ProfileContent'>
                        <h3>Please login with Google in order to see your profile</h3>
                    </div>
            }
        </div>
        );
}