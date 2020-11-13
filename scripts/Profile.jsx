import React, {useState,useEffect} from 'react';

import { Socket } from './Socket';

export function Profile(props) {
    const currentUser = props.currentUser;
    const [isEdit, setStatus] = useState(false);
    const profileDetail = props.profileDetail;
    console.log(props);
    
    function updateStatus() {
        setStatus((prevStatus) => !isEdit);
    }
    
    function handleSubmit(event) {
        let weight = document.getElementById("weight").value;
        let activityLevel = document.getElementById("ActivityLevel").value;
        
        if (weight == '' || weight == 'e'){
            alert('Please type in a valid weight');
        }
        if (activityLevel == '0'){
            alert("Please select an activity level option");
        }
        else{
            weight = parseFloat(weight);
            setStatus((prevStatus) => !isEdit);
            Socket.emit('updated user input',{
              'weight': weight,
              'activityLevel': activityLevel
            });
        }
        event.preventDefault();
    }
    console.log("profileDetail", profileDetail);
    
    return (
        <div>
            <h1> { currentUser.name } </h1><br/>
            <label>Height: { profileDetail.height }</label><br/>
            <label>Age:{ profileDetail.age }</label><br/>
            <label>Gender:{ profileDetail.gender }</label><br/>
            <label>Activity Level:{ profileDetail.activityLevel }</label><br/>
            <label>Estimated Weight Gain: </label><br/>
            { isEdit? 
                <form onSubmit={ handleSubmit }>
                    <h2> Updates</h2>
                    <label>Weight: </label>
                    <input type="number" id="weight"  placeholder="lbs" /> lbs<br/><br/>
                    <label>Activity Level: </label>
                        <select id="ActivityLevel">
                            <option value="0"> Please select the option Below</option>
                            <option value="1"> Somewhat Active</option>
                            <option value="2"> Exercise 1 - 3 times a week</option>
                            <option value="3"> Exercise 4 - 5 times a week</option>
                            <option value="4"> Daily Exercise or intense exercise 3 - 4 times a week</option>
                            <option value="5"> Intense Exercise 6 times a week</option>
                        </select><br/><br/>
                    <button type="submit">Submit</button>
                </form>
                :
                <button onClick = { updateStatus }>Edit</button>
            }
        </div>
        );
}