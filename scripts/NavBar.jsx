import React, { useState } from "react";
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
            <Home currentUser = { currentUser } />
          </Route>
          <Route path="/profile">
            <Profile currentUser = { currentUser } />
          </Route>
          <Route path="/foodsearch">
            <FoodSearch currentUser = { currentUser } />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

