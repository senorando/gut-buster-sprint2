import React, { useState } from "react";

import { UserForm } from "../UserForm";
import { Chat } from '../Chat/Chat';

export function HomeCont(props) {
  const currentUser = props.currentUser;
  const isLoggingIn = props.isLoggingIn;

  return (
    <div id = 'HomeContent'>
      { isLoggingIn?
        <UserForm />
        :
        <div className = 'Home'>
          { currentUser.isLoggedIn?
            <h3>Welcome { currentUser.name }</h3>              
            :
            <h3>Welcome! Please login to use Gut Buster</h3>
          }
          <div>
            <ul>
              <li>Gut Buster is a great fitness tool for all your daily fitness needs.</li><br/>
              <li>Once signed in you can view your profile, you can interact with other active users in our live chat</li><br/>
              <li>Once logged in you will be promped to fill out the information such as birthday, height, weight, goal weight, and activity level.</li><br/>
              <li>Navigate to Profile where our cutting edge software! will process all of the information and provide statistical information such as such as pie-chart for your macros, 
              line graph for goal weight, and the recommended meal based on your macros </li> <br/>
              <li>Navigate to Workout Log where you will be promped to fill out couple of information such as difficulty level and select workout splits.</li><br/>
              <li> Once you fill out the information our tool will provide you with workout plan for the full week.</li><br/>
              <li>Naviagte to the Food Search Page where you can enter any food and our tool will provide you with randomly suggested meals 
              with calorie counts, and preperation time, and link to the recepie.</li><br/>
          </ul>
          </div>
        </div>
      }
      <Chat currentUser = { currentUser }/>
    </div>
    );
}
