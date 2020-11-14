import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import { Socket } from './Socket';
import { Home } from "./Home";
import { Profile } from "./Profile";
import { FoodSearch } from "./FoodSearch";

export function NavBar() {
  const [currentUser, setUser] = useState({
      name: '', email: '', sid: '', isLoggedIn: false,
  });
  const [profileDetail, setProfileDetail] = useState({ 
        height: '', age: '', gender: '', activityLevel: '',
  });
  const [isLoggingIn, setStatus] = useState(false);
  console.log('NavBar: ' + isLoggingIn);
  
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
    });
  }
  function setDetails(){
    useEffect(() => {
      Socket.on('profile details',(data) => {
        if (data.id == currentUser.email ) {
          setProfileDetail((prevState) => ({
            height: data.height,
            age: data.age,
            gender: data.gender,
            activityLevel: data.activityLevel
          }));
        }
      });
      Socket.off('profile details','');
    });
  }
  function loginState(){
    useEffect(() => {
      Socket.on('is logging in', (data) => {
        console.log(data);
        setStatus((prevStatus) => true);
      });
      Socket.off('is logging in', '');
      Socket.on('is not logging in', (data) => {
        setStatus((prevStatus) => false);
      });
      Socket.off('is not logging in', '');
    });
  }
  
  setCurrUser();
  setDetails();
  loginState();
  return (
    <Router>
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/profile">Profile</Link>
          </li>
          <li>
            <Link to="/foodsearch">Food Search</Link>
          </li>
        </ul>

        <hr />
        <Switch>
          <Route exact path="/">
            <Home currentUser = { currentUser } isLoggingIn = { isLoggingIn }/>
          </Route>
          <Route path="/profile">
            <Profile currentUser = { currentUser } profileDetail = { profileDetail } isLoggingIn = { isLoggingIn }/>
          </Route>
          <Route path="/foodsearch">
            <FoodSearch currentUser = { currentUser } isLoggingIn = { isLoggingIn }/>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

