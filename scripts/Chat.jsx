import React, { useState,useEffect } from "react";
import { Button } from './Button';
import { Socket } from './Socket';


export function Chat(props) {
  const currentUser = props.currentUser;
  const username = props.currentUser.name;
  const isLoggedIn = props.currentUser.isLoggedIn;
  const [message, setMessage] = React.useState([]);
  
  function getNewMessage() {
        React.useEffect(() => {
            Socket.on('message received', (data) => {
                console.log("Received messages from server: " + data['allMessages']);
               setMessage(data['allMessages']);
            } )
        });
  }
  getNewMessage();
  return (
    <div>
        <h3>Live Chat Interaction: </h3>
        <ul>
        {
          message.map((messages, index) =>  
          <li key={index}><img src={messages.image} width="25" height="25"/> {messages.name}: {messages.text}</li>)
        }
        </ul>
         <Button currentUser = { currentUser } />
    </div>
    );
}