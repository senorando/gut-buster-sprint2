import React, { useState, useEffect } from 'react';
import ReactStars from "react-rating-stars-component";
import { Socket } from './Socket';

export function RatingStar(){
  const [AverageRating, setAverageRating] = useState([]);
  
  
  function ratingChanged(newRating) {
    console.log(newRating);
    let totalRating = 1;
    let oldRating = 3;
    setAverageRating((oldRating + newRating) / totalRating);
    Socket.emit('new rating', {
      'rating': AverageRating,
      'no_of_rating': totalRating
    })
  }
  
  return(
    <ReactStars
      count={5}
      value={AverageRating}
      onChange={ratingChanged}
      size={24}
      activeColor="#ffd700"
    />
    );
}