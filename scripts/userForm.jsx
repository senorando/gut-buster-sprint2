import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';
import {Profile} from './Profile'

function handleSubmit(event) {
    let age = document.getElementById("age");
    let height_inch=document.getElementById("height_inches");
    let weight=document.getElementById("weight");
    let gender=document.getElementById("gender");
    let gainOrLose = document.getElementById("GainLose");
    let activityLevel=document.getElementById("ActivityLevel");
    Socket.emit('new user input',{
      'age ': age,
      'height':height_inch,
      'weight':weight,
      'gender':gender,
      'gainOrLose':gainOrLose,
      'activityLevel':activityLevel
    });
    
    age = 0;
    height_inch=0;
    weight=0;
    event.preventDefault();
    ReactDOM.render(<Profile/>, document.getElementById('content'));
}

export function UserForm(){
  return(
        <form onSubmit={handleSubmit}>
            <h1>User Information</h1>
            <label for="age">Age:</label>
            <input type="number"  id="age"  name="age"/><br></br>
             <label for="height">Height:</label>
             <input type="number" id="height_inches" placeholder="ft"  name="height"/> ex: 5.10 feet <br></br>
             <label for="weight">Weight:</label>
             <input type="number" id="weight"  placeholder="lbs" /> lbs<br></br>
             <label for="gender">Gender:</label>
             <select id="gender">
                 <option value="men">Men</option>
                 <option value="women">Women</option>

             </select>
             <br></br>
              <label for="GainLose">Do you want to lose  your weight or gain ?</label>
             <select id="GainLose">
                 <option value="gain">Gain</option>
                 <option value="lose">Lose</option>
             </select><br></br>
             <p>How may pounds?
              <input type="number" id= "weightPound" placeholder="lbs"/> lbs 
            </p>
            <p><li>
                Activity Level: 
                1 = Somewhat Active
                2 = Exercise 1 - 3 times a week
                3 = Exercise 4 - 5 times a week
                4 = Daily Exercise or intense exercise 3 - 4 times a week
                5 = Intense Exercise 6 times a week
            </li> </p>
            <label for="ActivityLevel">Activity Level:</label>
             <select id="ActivityLevel">
                 <option value="1">1</option>
                 <option value="2">2</option>
                 <option value="3">3</option>
                 <option value="4">4</option>
                 <option value="5">5</option>
             </select><br></br>
             <button>Submit</button>
        </form>
        );
    }
