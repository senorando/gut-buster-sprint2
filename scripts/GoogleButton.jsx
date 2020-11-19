import React from 'react';
import ReactDOM from 'react-dom';
import { GoogleLogin, GoogleLogout } from 'react-google-login';
import { Socket } from './Socket';


const clientId = '235867645579-njgvhgfemvt05oh0hoj0eotb98dslr47.apps.googleusercontent.com';

export function Login() {
  const onSuccess = (res) => {
    let data = {
            'name': res.profileObj.name,
            'email': res.profileObj.email,
            'imgUrl': res.profileObj.imageUrl
        };
    console.log('|Login Success| currentUser: ', data);
    Socket.emit('google sign in', (data));
    
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
    Socket.emit('google sign out', 'User has successfully logged out');
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