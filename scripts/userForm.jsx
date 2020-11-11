import React, { useState } from "react";
import { Socket } from './Socket';
import ReactDOM from 'react-dom';

export function UserForm(){
    const [newUsr,setUsr]=useState('');
    Socket.on('new form',(data)=>{
       setUsr(data); 
    });
    Socket.off('new form',' ');
function handleSubmit(event) {
    let age = document.getElementById("age").value;
    let height_inch=document.getElementById("height_inches").value;
    let weight=document.getElementById("weight").value;
    let gender=document.getElementById("gender").value;
    let gainOrLose = document.getElementById("GainLose").value;
    let activityLevel=document.getElementById("ActivityLevel").value;
    
    console.log("age",age);
    console.log("hight",height_inch);
    console.log("weight",weight);
    console.log("gender",gender);
    console.log("gainOrLose",gainOrLose);
    console.log("activityLevel",activityLevel);
    Socket.emit('new user input',{
      'age': age,
      'height':height_inch,
      'weight':weight,
      'gender':gender,
      'gainOrLose':gainOrLose,
      'activityLevel':activityLevel,
      'name':newUsr.name,
      'email':newUsr.email
    });
    
    event.preventDefault();
}

  return(
        <form onSubmit={handleSubmit}>
            <h1>User Information</h1>
            <label>Age:</label>
            <input type="number"  id="age"  name="age"/><br></br>
             <label>Height:</label>
             <input type="number" id="height_inches" placeholder="ft"  name="height"/> e.g. 5.10 Feet ~= 61.2 inches<br></br>
             <label>Weight:</label>
             <input type="number" id="weight"  placeholder="lbs" /> lbs<br></br>
             <label>Gender:</label>
             <select id="gender">
                 <option value="men">Men</option>
                 <option value="women">Women</option>

             </select>
             <br></br>
              <label>Do you want to lose  your weight or gain ?</label>
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
            <label>Activity Level:</label>
             <select id="ActivityLevel">
                 <option value="1">1</option>
                 <option value="2">2</option>
                 <option value="3">3</option>
                 <option value="4">4</option>
                 <option value="5">5</option>
             </select><br></br>
             <button type="submit" value="Submit">Submit</button>
        </form>
        );
    }