import React, { useState, useEffect } from 'react';

import { MacrosChart } from './MacrosChart';
import { WeightGraph } from './WeightGraph';
import { UpdateForm } from './UpdateForm';
import { Socket } from '../Socket';

export function ProfileCont(props){
    console.log(props);
    const currentUser = props.currentUser;
    const [isEdit, setStatus] = useState(false);
    const profileDetail = props.profileDetail;
    const userWeight = props.userWeight;
    
    function updateStatus() {
        console.log('isEdit: ' + isEdit);
        setStatus((prevStatus) => !isEdit);
    }
    Socket.on('not editing', (data) => {
        console.log(data);
        setStatus(false);
    });
    Socket.off('not editing', '');
    return (
        <div>
            <div id = 'UserDetails'>
                <h1> { currentUser.name } </h1><br/>
                <label>Height: { profileDetail.height }</label><br/>
                <label>Weight: { userWeight[ userWeight.length - 1 ] }</label><br/>
                <label>Age: { profileDetail.age }</label><br/>
                <label>Gender: { profileDetail.gender }</label><br/>
                <label>Activity Level: { profileDetail.activityLevel }</label><br/>
                <label>BMR: { profileDetail.bmr }</label><br/>
                { isEdit? 
                    <div id = 'UserForm'>
                        <UpdateForm currentUser = { currentUser }/>
                    </div>
                    :
                    <button onClick = { updateStatus }>Add New Weight Entry</button>
                }
            </div>
            <div id = 'Macros'>
                <h3>Recommended Macros</h3><br/>
                <MacrosChart profileDetail = { profileDetail } />
            </div>
            <div id = 'Recommended Meals'>
                <h3>Recommended Meals based on your macros</h3>
                <label>Breakfast: { profileDetail.breakfastMeal }</label><br/>
                <label>Lunch: { profileDetail.lunchMeal }</label><br/>
                <label>Dinner: { profileDetail.dinnerMeal }</label><br/>
                <label>Total Calories: { profileDetail.calMeal }</label><br/>
                <label>Total Protein: { profileDetail.protMeal }</label><br/>
                <label>Total Carbs: { profileDetail.carbMeal }</label><br/>
                <label>Total Fat: { profileDetail.fatMeal }</label><br/>
            </div>
            <WeightGraph userWeight = { userWeight } />
        </div>
    );
}