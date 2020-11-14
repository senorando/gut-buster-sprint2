import React, { useState, useEffect } from 'react';

import { Socket } from './Socket';

export function UpdateForm(props) {
    const currentUser = props.currentUser;
    
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
            Socket.emit('new entry',{
              'weight': weight,
              'email': currentUser.email,
              'sid': currentUser.sid
            });
        }
        event.preventDefault();
    }
    
    return (
        <form onSubmit={ handleSubmit }>
            <h3>Add a new entry</h3>
            <label>Weight: </label>
            <input type="number" id="weight"  placeholder="lbs" /> lbs<br/><br/>
            <button type="submit">Submit</button>
        </form>
    )
}