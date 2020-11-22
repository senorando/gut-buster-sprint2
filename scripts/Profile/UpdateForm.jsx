import React, { useState, useEffect } from 'react';

import { Socket } from '../Socket';

export function UpdateForm(props) {
    const currentUser = props.currentUser;
    
    function handleSubmit(event) {
        let weight = parseFloat(document.getElementById("weight").value);
        
        if (weight == '' || weight == 'e'){
            alert('Please type in a valid weight');
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
            Weight: <input type="float" id="weight"  placeholder="lbs" /> lbs<br/><br/>
            <button type="submit">Submit</button>
        </form>
    )
}