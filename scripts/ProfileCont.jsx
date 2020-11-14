import React, { useState, useEffect } from 'react';

import { UpdateForm } from './UpdateForm';
import { Socket } from './Socket';

export function ProfileCont(props){
    const currentUser = props.currentUser;
    const [isEdit, setStatus] = useState(false);
    const profileDetail = props.profileDetail;
    function updateStatus() {
        setStatus((prevStatus) => !isEdit);
    }
    return (
        <div>
            <div id = 'UserDetails'>
                <h1> { currentUser.name } </h1><br/>
                <label>Height: { profileDetail.height }</label><br/>
                <label>Weight: TODO</label><br/>
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
                <h3>Recommended Macros based on your goals</h3><br/>
                <label>Max Calories: { profileDetail.maxCal }</label><br/>
                <label>Max Protein: { profileDetail.maxProt }</label><br/>
                <label>Max Carbs: { profileDetail.maxCarb }</label><br/>
                <label>Max Fat: { profileDetail.maxFat }</label><br/>
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
        </div>
    );
}