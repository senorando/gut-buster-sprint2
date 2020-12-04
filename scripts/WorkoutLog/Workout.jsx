import React, { useState, useEffect } from 'react';

import { UserForm } from '../UserForm';
import { Socket } from '../Socket';
import {WorkoutForm } from './WorkoutForm';

export function Workout(props) {
    const currentUser = props.currentUser;
    const isLoggingIn = props.isLoggingIn;
    
    return (
        <div id = 'Workout'>
            { isLoggingIn?
                <div id = 'UserForm'>
                    <UserForm />
                </div>
                :
                <div id = 'WorkoutContent'>
                    <WorkoutForm currentUser = { currentUser } />
                </div>
            }
        </div>
    );
}