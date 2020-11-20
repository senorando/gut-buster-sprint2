import * as React from 'react';
import { Socket } from './Socket';

export function Button(props) {
    const currentUser = props.currentUser;
    const isLoggedIn = props.currentUser.isLoggedIn;
    console.log(isLoggedIn);
    
    function handleSubmit(event) {
        let newtexts = document.getElementById("text_input");
  
        Socket.emit('new text input',{
            'entry': newtexts.value+'',
            'email': currentUser.email
        });
        
    console.log('Sent the message ' + newtexts.value + ' to server!');
    newtexts.value = ''
    event.preventDefault();
    }
    
    return (
        <form onSubmit={handleSubmit}>
            <div className="bottom container">
            { isLoggedIn?
            <div>
            <input id="text_input" placeholder="Enter a Text! "></input>
            <button>Submit</button>
            </div>
            :
            <h1>Please log in to chat</h1>
            }
            </div>
        </form>
    );
}
