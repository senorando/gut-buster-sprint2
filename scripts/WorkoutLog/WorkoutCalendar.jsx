import React, { useState, useEffect } from 'react';
import Calendar from 'react-calendar';

import { Socket } from '../Socket';

export function WorkoutCalendar(props){
    const currentUser = props.currentUser;
    const workout_plan = props.workout_plan;
    console.log(workout_plan);
    
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var d = new Date();
    var today = days[d.getDay()];
    
    const daysList = days.map((day, index) => {
        return (
            <div className = { day == today? 'Today' : 'OtherDay' } key = { index }>
                <div id = 'DateHead'>
                    <h2>{ day }</h2>
                </div>
                <div id = 'DateBody'>
                    { exerciseList(index) }
                </div>
            </div>
        );
    });
    
    function exerciseList(index) {
        
        return (
            index < workout_plan.length? 
                <div id = 'Exercises'>
                    <h3>{ workout_plan[index].title }</h3><br/>
                    { workout_plan[index].workout.map((exercise, windex) => {
                    let name = exercise.name;
                    console.log(name);
                    
                    return(
                            <div id = 'Exercise'>
                                { name }
                            </div>
                        );
                    })}
                </div>
                :
                <div id = 'blank'></div>
        );
    }
    return(
        <div className = 'Calendar'>
            { daysList }
        </div>
    );
}