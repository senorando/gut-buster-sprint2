import React, { useState } from "react";

import { Socket } from '../Socket';

import { HomeCont } from './HomeCont';

export function Home(props) {
  const currentUser = props.currentUser;
  const isLoggingIn = props.isLoggingIn;
  
  return (
    <HomeCont currentUser = { currentUser } isLoggingIn = { isLoggingIn }/>
    );
}
    
