import * as React from 'react';
import { Socket } from './Socket';


export function Profile(props) {
    const currentUser = props.currentUser;
    
    console.log(currentUser);
    
    // Socket.emit('update user input',{
    //   'weight': props.name,
    //   'activityLevel':props.email
    // });
    return (
        
        <div>
                <h1> User Profile </h1>
                <h2> User name : { currentUser.name }</h2><br></br>
                <label >Weight Goal:</label><br></br>
                <label >Activity Level:</label><br></br>
                <label>Estimated Waight Gain/Lose:</label><br></br>
            <h2> Updates</h2>
            <label>Weight:</label>
            <input type="number" id="weight"  placeholder="lbs" /> lbs<br></br>
            <label>Activity Level:</label><br></br>
             <select id="ActivityLevel">
                 <option value="1">1</option>
                 <option value="2">2</option>
                 <option value="3">3</option>
                 <option value="4">4</option>
                 <option value="5">5</option>
             </select><br></br>
             <button>Done</button>
         </div>
        );
}