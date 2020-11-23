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
        <div id = 'ProfileContent'>
            <div id = 'Left'>
                <div className = 'UserDetails'>
                    <h3> { currentUser.name } </h3><br/>
                    <p>
                        Height: { profileDetail.height } <br/>
                        Weight: { userWeight[ userWeight.length - 1 ] } <br/>
                        Age: { profileDetail.age } <br/>
                        Gender: { profileDetail.gender } <br/>
                        Activity Level: { profileDetail.activityLevel } <br/>
                        BMR: { profileDetail.bmr } <br/>
                    </p>
                    { isEdit? 
                        <UpdateForm currentUser = { currentUser }/>
                        :
                        <button onClick = { updateStatus }>Add New Weight Entry</button>
                    }
                </div>
                <MacrosChart profileDetail = { profileDetail } />
            </div>
            <div id = 'Right'>
                <WeightGraph userWeight = { userWeight } />
                <div className = 'RecommendedMeals'>
                    <h3>Recommended Meals based on your macros</h3>
                    <p>
                        Breakfast: { profileDetail.breakfastMeal } <br/>
                        Lunch: { profileDetail.lunchMeal } <br/>
                        Dinner: { profileDetail.dinnerMeal } <br/>
                        Total Calories: { profileDetail.calMeal } <br/>
                        Total Protein: { profileDetail.protMeal } <br/>
                        Total Carbs: { profileDetail.carbMeal } <br/>
                        Total Fat: { profileDetail.fatMeal } <br/>
                    </p>
                </div>
            </div>               
        </div>
    );
}