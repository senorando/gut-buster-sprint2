import React, { useState, useEffect } from 'react';

import { UserForm } from '../UserForm';
import { Socket } from '../Socket';
import { WorkoutForm } from './WorkoutForm';
import { WorkoutCalendar } from './WorkoutCalendar';

export function Workout(props) {
    const currentUser = props.currentUser;
    const hasPlan = currentUser.hasPlan;
    const workout_plan = props.workout_plan;
    const isLoggingIn = props.isLoggingIn;
    console.log(workout_plan);
    console.log(hasPlan);
    
    return (
        <div id = 'Workout'>
            { isLoggingIn?
                <UserForm />
                :
                <div id = 'WorkoutContent'>
                    { currentUser.isLoggedIn?
                        hasPlan?
                            <WorkoutCalendar currentUser = { currentUser } 
                                                workout_plan = { workout_plan }/>
                            :
                            <WorkoutForm currentUser = { currentUser } />
                        :
                        <h3>Please login to use this feature!</h3>
                    }
                    
                </div>
            }
        </div>
    );
}