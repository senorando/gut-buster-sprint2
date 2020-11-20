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
    
    if (document.getElementById("age").value == "" ){
        
        alert("Please enter a value for age")
        
    }
    if (document.getElementById("height_feet").value == ""){
        alert("Please enter a value for feet")
    }
   if (document.getElementById("height_inches").value == "" ){
        alert("Please enter a value for inches")
    }
    if (document.getElementById("weight").value == ""  ){
        alert("Please enter a value for weight")
    
    }
    if (document.getElementById("gender").value == "0"){
        alert("Please select your gender ");
    }
  
    if (document.getElementById("GainLose").value == "0"){
        alert("Please select your weight goals ");
     
    }
     if (document.getElementById("weightPound").value == "" ){
        alert("Please enter a value for how much weight you want to gain/lose ");
    }
    
    if (document.getElementById("ActivityLevel").value == "0"){
        alert("Please select an activity level option ");
     
    }
   else{
    let age = parseInt(document.getElementById("age").value);
    let height_feet= parseInt(document.getElementById("height_feet").value);
    let height_inch=parseInt(document.getElementById("height_inches").value);
    let weight=parseFloat(document.getElementById("weight").value);
    let gender=document.getElementById("gender").value;
    let gainOrLose = document.getElementById("GainLose").value;
    let activityLevel=document.getElementById("ActivityLevel").value;
    
    let height = (height_feet * 12 ) + height_inch;
   
    Socket.emit('new user input',{
      'age': age,
      'height':height,
      'weight':weight,
      'gender':gender,
      'gainOrLose':gainOrLose,
      'activityLevel':activityLevel,
      'name':newUsr.name,
      'email':newUsr.email,
      'imgUrl': newUsr.imgUrl,
    });
   }
    
    event.preventDefault();
}

  return(
        <form onSubmit={handleSubmit}>
            <h1>User Information</h1>
            <label>Age:</label>
            <input type="number"  id="age"  name="age"/><br></br>
             <label>Height :</label>
             <input type="number" id="height_feet" placeholder="feet"  name="height"/> 
             <input placeholder="inches" id="height_inches"/><br/>
             <label>Weight:</label>
             <input type="number" id="weight"  placeholder="lbs" /> lbs<br></br>
             <label>Gender:</label>
             <select id="gender">
                 <option value="0"> Please select the gender</option>
                 <option value="men">Men</option>
                 <option value="women">Women</option>

             </select>
             <br></br>
              <label>Do you want to lose  your weight or gain ?</label>
             <select id="GainLose">
                 <option value="0">Please select your goal</option>
                 <option value="gain">Gain</option>
                 <option value="lose">Lose</option>
             </select><br></br>
             <p>How may pounds?
              <input type="number" id= "weightPound" placeholder="lbs"/> lbs 
            </p>
            <label>Activity Level:</label>
             <select id="ActivityLevel">
                 <option value="0"> Please select the option Below</option>
                 <option value="1"> Somewhat Active</option>
                 <option value="2"> Exercise 1 - 3 times a week</option>
                 <option value="3"> Exercise 4 - 5 times a week</option>
                 <option value="4"> Daily Exercise or intense exercise 3 - 4 times a week</option>
                 <option value="5"> Intense Exercise 6 times a week</option>
             </select><br></br>
             <button type="submit" value="Submit">Submit</button>
        </form>
        );
    }