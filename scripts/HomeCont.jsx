import React, { useState } from "react";


export function HomeCont(props) {
  const currentUser = props.currentUser;

  return (
    <div>
        <h3>Welcome to the Gut Buster { currentUser.name }</h3>
        <p>
            We aim to provide healthy food instructions,<br></br>
            diet plans and deliver a live chat accessible from the browser.<br></br>
            The  web app will provide a social login to allow users to easily identify themselves,<br></br>
            and feature a Comment/Discussion attitude, through that people can communicate with each other .
        </p>
    </div>
    );
}
