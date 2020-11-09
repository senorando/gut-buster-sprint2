import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';

function handleSubmit(event) {
    let age = document.getElementById("age");
    let height_inch=document.getElementById("height_inches");
    let weight=document.getElementById("weight");
    let gender=document.getElementById("gender");
    let protine=document.getElementById("protine");
    let gainOrLose = document.getElementById("GainLose");
    let activityLevel=document.getElementById("ActivityLevel");
    Socket.emit('new user input',{
      'age ': age,
      'height_inch':height_inch,
      'weight':weight,
      'gender':gender,
      'protine':protine,
      'gainOrLose':gainOrLose,
      'activityLevel':activityLevel
    });
    
    age = 0;
    height_inch=0;
    weight=0;
    protine='';
    event.preventDefault();
    ReactDOM.render(<profileContent/>, document.getElementById('content'));
}

export function UserForm(){
  return(
        <form onSubmit={handleSubmit}>
            <h1>User Information</h1>
            <label for="age">Age:</label>
            <input type="number"  id="age"  name="age"/><br></br>
             <label for="height">Height:</label>
             <input type="number" id="height_inches" placeholder="ft"  name="height"/> ex: 5.10 feet ~= 60 inches <br></br>
             <label for="weight">Weight:</label>
             <input type="number" id="weight"  placeholder="lbs" /> lbs<br></br>
             <label for="gender">Gender:</label>
             <select id="gender">
                 <option value="man">Man</option>
                 <option value="woman">Woman</option>
                 <option value="other">Other</option>
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
            <p> What kind of protine do you want to have in your food? 
              <input type="text" id= "protine" placeholder="protine"/> 
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
             </select>
             <button>Submit</button>
        </form>
        );
    }
