import * as React from 'react';
import { Socket } from './Socket';


export function Profile() {
    let weight=document.getElementById("weight");
    let activityLevel=document.getElementById("ActivityLevel");
    Socket.emit('update user input',{
      'weight':weight,
      'activityLevel':activityLevel
    });
    return (
        <body>
            <h1> User Profile </h1>
        <div>
                <h2> User name : </h2><br></br>
                <label >Weight Gole:</label><br></br>
                <label >Activity Level:</label><br></br>
                <label>Estimated Waight Gain/Lose:</label><br></br>
        </div>
         <div>
            <h2> Updates</h2>
            <label for="weight">Weight:</label>
            <input type="number" id="weight"  placeholder="lbs" /> lbs<br></br>
            <label for="ActivityLevel">Activity Level:</label><br></br>
             <select id="ActivityLevel">
                 <option value="1">1</option>
                 <option value="2">2</option>
                 <option value="3">3</option>
                 <option value="4">4</option>
                 <option value="5">5</option>
             </select><br></br>
             <button>Done</button>
         </div>
         </body>
        );
}