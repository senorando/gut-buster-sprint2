import React, { useState,useEffect } from "react";
import { animateScroll } from 'react-scroll';

import { Button } from './Button';
import { Socket } from '../Socket';


export function Chat(props) {
  const currentUser = props.currentUser;
  const isLoggedIn = props.currentUser.isLoggedIn;
  const [message, setMessage] = useState([]);
  
  function scroll() {
    animateScroll.scrollToBottom({
      containerId: 'Message_List',
    });
  }
  function getNewMessage() {
        useEffect(() => {
            Socket.on('message received', (data) => {
                console.log("Received messages from server: " + data['allMessages']);
               setMessage(data['allMessages']);
            });
            Socket.off('message received', '');
        }, []);
  }
  useEffect(() => { scroll(); }, []);
  getNewMessage();
  return (
    <div id = 'ChatBox'>
        <h3>Live Chat</h3>
        <ul id = 'Message_List'>
        { message.map((messages, index) =>  
            <li id = 'Message' key={index}>
              <div id = {index % 2 === 1? 'MessageTextOdd' : 'MessageTextEven'}>
                <img id = 'Profile_Pic' src={messages.image}/> {messages.name}: {messages.text}
              </div>
            </li>
        )}
        </ul>
        <Button currentUser = { currentUser } />
    </div>
    );
}