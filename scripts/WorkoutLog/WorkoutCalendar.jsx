import React, { useState, useEffect } from 'react';
import Calendar from 'react-calendar';

import { Socket } from '../Socket';

export function WorkoutCalendar(props){
    const currentUser = props.currentUser;
    const workout_plan = props.workout_plan;
    console.log(workout_plan);
    var count = -1;
    
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var d = new Date();
    var today = days[d.getDay()];
    const [selected, setSelected] = useState(
        ['Monday', 'Tuesday', 'Thursday', 'Friday']
    );
    
    const daysList = days.map((day, index) => {
        return (
            selected.indexOf(day) >= 0? 
                        <div className = { day == today? 'Today' : 'OtherDay' } key = { index }>
                            <div id = 'DateHead'>
                                <h2>{ day }</h2>
                            </div>
                            <div id = 'DateBody'>
                                { exerciseList(index) }
                            </div> 
                        </div>
                        :
                        <div className = { day == today? 'Today' : 'OtherDay' } key = { index }>
                            <div id = 'DateHead'>
                                <h2>{ day }</h2>
                            </div>
                            <div id = 'DateBody'>
                                <h2>REST</h2>
                            </div> 
                        </div> 
        );
    });
    
    function exerciseList(index) {
        
        if(count < workout_plan.length){
            count += 1;
            return(
                <div id = 'Exercises'>
                    <h3>{ workout_plan[count].title }</h3><br/>
                    { workout_plan[count].workout.map((exercise, windex) => {
                    let name = exercise.name;
                    console.log(name);
                    
                    return(
                            <div id = 'Exercise'>
                                { name }
                            </div>
                        );
                    })}
                </div>
            );
        }else{
            return(
                <div id = 'blank'></div>
            );
        }
    }
    return(
        <div className = 'Calendar'>
            { daysList }
        </div>
    );
}