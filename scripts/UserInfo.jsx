
import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    let newAddress = document.getElementById("weight_input");
   
    // TODO- send the address on. a socket to the server
    Socket.emit('new address input',{
        'address': newAddress.value+'',});
    
    
    console.log('Sent the address ' + newAddress.value + ' to server!');
    newAddress.value = ''
    
    event.preventDefault();
}

export function Button() {
    return (
        <form onSubmit={handleSubmit}>
            <div className="bottom container">
            
            <h4> Hi there! Welcome New User!! </h4> 
            <h4> Create your new Profile Today by entering your information!! </h4>
            <label>Enter your Weight in Pounds(lbs): </label>
            <input id="weight_input" placeholder="Enter in lbs "></input><br/>
            <label>Enter your Height in Inches: </label>
            <input id="height_input" placeholder="Enter in inches "></input><br/>
            <label>Enter your Age: </label>
            <input id="age_input" placeholder="Enter your age "></input><br/>
            <label>Enter your Gender(Male/Female): </label>
            <input id="gender_input" placeholder="Enter m/f "></input><br/>
            <select name = "dropdown">
            <option value = "Somewhat Active" selected>Somewhat Active</option>
            <option value = "Exercise 1 - 3 times a week">Exercise 1 - 3 times a week</option>
            <option value = "Exercise 4 - 5 times a week">Exercise 4 - 5 times a week</option>
            <option value = "Daily Exercise or intense exercise 3 - 4 times a weekk">Daily Exercise or intense exercise 3 - 4 times a week</option>
            <option value = "Intense Exercise 6 times a week">Intense Exercise 6 times a week</option>
            </select><br/>
            <div className="buttonbucket">
            <button>Submit</button>
            </div>
            </div>
        </form>
    );
}
