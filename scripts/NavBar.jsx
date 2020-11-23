import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import { Login, Logout} from './GoogleButton';
import { Socket } from './Socket';
import { Home } from "./Home/Home";
import { Profile } from "./Profile/Profile";
import { Workout } from './WorkoutLog/Workout';
import { FoodSearch } from "./FoodSearch/FoodSearch";

export function NavBar() {
  const [currentUser, setUser] = useState({
      name: '', email: '', sid: '', isLoggedIn: false,
  });
  const [profileDetail, setProfileDetail] = useState({ 
        height: '', age: '', gender: '', activityLevel: '',
  });
  const [userWeight, setWeight] = useState([]);
  const [isLoggingIn, setStatus] = useState(false);
  function setCurrUser(){
    useEffect(() => {
      Socket.on('success login', (data) => {
        if (data.sid === Socket.id) {
          setUser((prevState) => ({
            name: data.name,
            email: data.email,
            sid: data.sid,
            isLoggedIn: true,
          }));
        }
      });
      Socket.off('success login', '');
      Socket.on('success logout', (data) => {
        if (data.sid === Socket.id) {
          setUser((prevState) => ({
            name: '',
            email: '',
            sid: data.sid,
            isLoggedIn: false,
          }));
          setProfileDetail((prevState) => ({
            height: '',
            age: '',
            gender: '',
            activityLevel: '',
            bmr: '',
            maxCal: '',
            maxProt: '',
            maxCarb: '',
            maxFat: '',
            breakfastMeal: '',
            lunchMeal: '',
            dinnerMeal: '',
            calMeal: '',
            carbMeal: '',
            protMeal: '',
            fatMeal: '',
          }));
          setWeight([]);
          console.log('You have successfully logged out!');
        }
      });
      Socket.off('success logout', '');
    }, []);
  }
  function setDetails(){
    useEffect(() => {
      Socket.on('profile details',(data) => {
        if (data.id == currentUser.email ) {
          console.log(data);
          setProfileDetail((prevState) => ({
            height: data.height,
            age: data.age,
            gender: data.gender,
            activityLevel: data.activityLevel,
            bmr: data.bmr,
            maxCal: data.maxCal,
            maxProt: data.maxProt,
            maxCarb: data.maxCarb,
            maxFat: data.maxFat,
            breakfastMeal: data.breakfastMeal,
            lunchMeal: data.lunchMeal,
            dinnerMeal: data.dinnerMeal,
            calMeal: data.calMeal,
            carbMeal: data.carbMeal,
            protMeal: data.protMeal,
            fatMeal: data.fatMeal,
          }));
        }
      });
      Socket.off('profile details','');
      Socket.on('most recent weight', (data) => {
        if(data.sid === Socket.id){
          console.log('data.weight: ' + data.weight);
          setWeight(data.weight);
        }
      });
      Socket.off('most recent weight', '');
    });
  }
  
  function UserDetails(){
    useEffect(() => {
      Socket.on('User Details',(data) => {
        console.log('h')
        if (data.id == currentUser.email ) {
          console.log(data);
          setProfileDetail((prevState) => ({
            height: data.height,
            age: data.age,
            gender: data.gender,
            activityLevel: data.activityLevel,
            bmr: data.bmr,
            maxCal: data.maxCal,
            maxProt: data.maxProt,
            maxCarb: data.maxCarb,
            maxFat: data.maxFat,
            breakfastMeal: data.breakfastMeal,
            lunchMeal: data.lunchMeal,
            dinnerMeal: data.dinnerMeal,
            calMeal: data.calMeal,
            carbMeal: data.carbMeal,
            protMeal: data.protMeal,
            fatMeal: data.fatMeal,
          }));
        }
      });
      
      
    });
  }
  function loginState(){
    useEffect(() => {
      Socket.on('is logging in', (data) => {
        if(data.sid === Socket.id){
          console.log(data.res);
          setStatus((prevStatus) => true);
        }
      });
      Socket.off('is logging in', '');
      Socket.on('is not logging in', (data) => {
        setStatus((prevStatus) => false);
      });
      Socket.off('is not logging in', '');
    });
  }
  function failedLogin(){
    useEffect(() => {
      Socket.on('failed login', (data) => {
          alert(data.res);
      });
      Socket.off('failed login', '');
      
    }, []);
  }
  setCurrUser();
  setDetails();
  loginState();
  failedLogin();
  UserDetails();
  return (
    <div id = 'App'>
      <div id = 'AppHead'>
        <h1>Gut Buster</h1>
      </div>
      <Router>
        <div id = 'NavBar'>
          <Link  id = 'NavButton' to="/">
            Home
          </Link>
          <Link id = 'NavButton' to="/profile">
            Profile
          </Link>
          <Link id = 'NavButton' to="/workout">
            Workout Log
          </Link>
          <Link id = 'NavButton' to="/foodsearch">
            Food Search
          </Link>
          { currentUser.isLoggedIn?
            <Logout />
            :
             isLoggingIn?
              <button id = 'NavButton'><i>Logging In</i></button>
              :
              <Login />
          }
        </div>
            <hr />
        <Switch>
          <Route exact path="/">
            <Home currentUser = { currentUser } 
                  isLoggingIn = { isLoggingIn }/>
          </Route>
          <Route path="/profile">
            <Profile currentUser = { currentUser }
                      userWeight = { userWeight } 
                      profileDetail = { profileDetail } 
                      isLoggingIn = { isLoggingIn }/>
          </Route>
           <Route path="/workout">
            <Workout currentUser = { currentUser } 
                          isLoggingIn = { isLoggingIn }/>
          </Route>
          <Route path="/foodsearch">
            <FoodSearch currentUser = { currentUser } 
                          isLoggingIn = { isLoggingIn }/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

