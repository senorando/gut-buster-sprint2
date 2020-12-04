import React, { useState, useEffect } from 'react';

import { Socket } from '../Socket';

export function Day(props) {
    const currentUser = props.currentUser;
    
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var d = new Date();
    var today = days[d.getDay()];
    const [plan, setPlan] = useState();
    
    function getWorkoutPlan() {
        useEffect(() => {
            Socket.on('workouts received', (data) => {
                if(data.sid === currentUser.sid){
                    setPlan(data);
                }
            });
            Socket.off('workouts received', '');
        }, []);
    }
    
    getWorkoutPlan();
    
    const daysList = days.map((day, index) => {
        return (
            <div className = { day == today? 'Today' : 'OtherDay' } key = { index }>
                <div id = 'DateHead'>
                    <h3>{ day }</h3>
                </div>
                <div id = 'DateBody'>
                    <p>{ plan }</p>
                </div>
            </div>
        );
    });
    return(
        <div className = 'Calendar'>
            { daysList }
        </div>
    );
}