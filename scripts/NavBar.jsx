import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { Home } from "./Home";
import { Profile } from "./Profile";
import { FoodSearch } from "./FoodSearch";

export function NavBar() {
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
            <Home />
          </Route>
          <Route path="/profile">
            <Profile />
          </Route>
          <Route path="/foodsearch">
            <FoodSearch />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

