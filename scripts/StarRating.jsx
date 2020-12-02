import * as React from 'react';
import ReactStars from "react-rating-stars-component";

export function RatingStar(){
  function ratingChanged(newRating) {
    console.log(newRating);
  }
  
  return(
    <ReactStars
      count={5}
      onChange={ratingChanged}
      size={24}
      activeColor="#ffd700"
    />
    );
}