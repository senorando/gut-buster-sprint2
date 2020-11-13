import React, {useState,useEffect} from 'react';
import { Socket } from './Socket';



export function Profile(props) {
    const currentUser = props.currentUser;
    const [isEdit, setStatus] = useState(false);
    const [profileDetail,setProfileDetail]=useState({ 
        height:'',age:'',gender:'', activityLevel:''
    });
 
  
//   Socket.on('is logging in', (data) => {
//     console.log(data);
//     setStatus((prevStatus) => true);
//   });
//   Socket.off('is logging in', '');
//   Socket.on('is not logging in', (data) => {
//     setStatus((prevStatus) => false);
//   });
//   Socket.off('is not logging in', '');
  
  function setDetails(){
      useEffect(() => {
            Socket.on('profile details',(data) => {
                console.log("id:  " + data.id );
                setProfileDetail((prevState) => ({...prevState,
                height: data.height,
                age: data.age,
                gender: data.gender,
                activityLevel: data.activityLevel
                }));
            });
        Socket.off('profile details','');
        });
     
        //   Socket.on('profile details',(data) => {
        //       console.log("check socket");
        //           setDetail((prevState) => ({
        //               height: data.height,
        //               age:data.age,
        //               gender:data.gender,
        //               activityLevel:data.activityLevel
        //           }));
        //   });
    }
   
    function handleSubmit(event) {
        if (document.getElementById("ActivityLevel").value == "0"){
        alert("Please select an activity level option ");
        }
        else{
          let weight=parseFloat(document.getElementById("weight").value);
          let activityLevel=document.getElementById("ActivityLevel").value;
          Socket.emit('updated user input',{
              'weight': weight,
              'activityLevel': activityLevel
          });
        }
     
      event.preventDefault();
      
    }
    
    
  setDetails();
  set_height()
  console.log("profileDetail", profileDetail);
    
return (
        <div>
                <h1> User Profile </h1>
                <h2> User name : { currentUser.name }</h2><br></br>
                <label>Height: {Height}</label><br></br>
                <label>Age:{ profileDetail.age }</label><br></br>
                <label>Gender:{ profileDetail.gender }</label><br></br>
                <label>Activity Level:{ profileDetail.activityLevel }</label><br></br>
                <label>Estimated Waight Gain/Lose:</label><br></br>
         <form onSubmit={handleSubmit}>
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
         </div>
        );
}