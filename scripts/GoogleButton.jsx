import React from 'react';
import ReactDOM from 'react-dom';
import { GoogleLogin, GoogleLogout } from 'react-google-login';

import { Socket } from './Socket';
import { Button } from './UserInfo';
import { Home } from './Home';

const clientId = '235867645579-gs14jqdef78eh8fads7d6ul1qv5gmf1r.apps.googleusercontent.com';

export function Login() {
  const onSuccess = (res) => {
    const user = res.profileObj;
    console.log('|Login Success| currentUser: ', user);
    Socket.emit('new google', (user));
    
  };
  const onFailure = (res) => {
    console.log('|Login Failed| res:', res);
  };
  return (
    <div id="GoogleLogin">
  
      <GoogleLogin
        clientId={clientId}
        buttonText="Login"
        onSuccess={onSuccess}
        onFailure={onFailure}
        cookiePolicy="single_host_origin"
      />
    </div>
  );
}
export function Logout() {
  const onSuccess = () => {
    alert('Successfully Logged Out!');
  };
  return (
    <div id="GoogleLogout">
      <GoogleLogout
        clientId={clientId}
        buttonText="Logout"
        onLogoutSuccess={onSuccess}
      />
    </div>
  );
}
