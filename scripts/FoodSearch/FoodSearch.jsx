import React, { useState, useEffect } from 'react';
import ReactStars from "react-rating-stars-component";
import { UserForm } from '../UserForm';
import { Socket } from '../Socket';
import SearchField from "react-search-field";

export function FoodSearch(props) {
    const isLoggingIn = props.isLoggingIn;
    const foodSearched = props.foodSearched;
    
    function ratingChanged(newRating) {
        console.log(newRating);
    }
    
    function handleSubmit(response) {
        console.log(response);
        let name = response;
        Socket.emit('new food search', {
          'food_search': name,
        });
       console.log('Sent the food ' + name + ' to server!');
    }
    
    const [food, setFoods] = useState([]);
    const [ingredient, setIngredient] = useState([]);
    const [prep, setPrep] = useState([]);
    const [image, setImage] = useState([]);
    
    
    const [food1, setFoods1] = useState([]);
    const [ingredient1, setIngredient1] = useState([]);
    const [prep1, setPrep1] = useState([]);
    const [image1, setImage1] = useState([]);
    
    const [food2, setFoods2] = useState([]);
    const [ingredient2, setIngredient2] = useState([]);
    const [prep2, setPrep2] = useState([]);
    const [image2, setImage2] = useState([]);
    
    const [food3, setFoods3] = useState([]);
    const [ingredient3, setIngredient3] = useState([]);
    const [prep3, setPrep3] = useState([]);
    const [image3, setImage3] = useState([]);
    
    const [food4, setFoods4] = useState([]);
    const [ingredient4, setIngredient4] = useState([]);
    const [prep4, setPrep4] = useState([]);
    const [image4, setImage4] = useState([]);
   
    const [food5, setFoods5] = useState([]);
    const [ingredient5, setIngredient5] = useState([]);
    const [prep5, setPrep5] = useState([]);
    const [image5, setImage5] = useState([]);   

    function GetFoodResponse() {
        useEffect(() => {
            Socket.on('food response', (data) => {
                setFoods(data[0][0]);
                setPrep(data[0][1] + " minutes prep time");
                setIngredient(data[0][2]);
                setImage(data[0][3]);
                console.log(data[0][3]);
                
                setFoods1(data[1][0]);
                setPrep1(data[1][1] + " minutes prep time");
                setIngredient1(data[1][2]);
                setImage1(data[1][3]);
                
                setFoods2(data[2][0]);
                setPrep2(data[2][1] + " minutes prep time");
                setIngredient2(data[2][2]);
                setImage2(data[2][3]);
                
                setFoods3(data[3][0]);
                setPrep3(data[3][1] + " minutes prep time");
                setIngredient3(data[3][2]);
                setImage3(data[3][3]);
                
                setFoods4(data[4][0]);
                setPrep4(data[4][1] + " minutes prep time");
                setIngredient4(data[4][2]);
                setImage4(data[4][3]);
                
                setFoods5(data[5][0]);
                setPrep5(data[5][1] + " minutes prep time");
                setIngredient5(data[5][2]);
                setImage5(data[5][3]);
                
            });
            Socket.off('food response', '');
        }, []);
    }
   
   GetFoodResponse();
   
   
        
    return (
         <div id = 'FoodSearch'>
            { isLoggingIn?
                <div id = 'UserForm'>
                    <UserForm />
                </div>
                :
                <div id = 'SearchContent'>
                    <h3>Food Search</h3>
                    <SearchField
                          placeholder="Search..."
                          classNames="test-class"
                          onSearchClick={handleSubmit}
                        /><br/>
                    <br/>
                    <div className="food">
                        <span><a target="_blank" href={ingredient}>{food}</a></span><br/>
                        <span>{prep}</span><br/>
                        <span><img src= {image}/></span><br/>
                        <br></br>
                    </div>
                    <div className="food1">
                        <span><a target="_blank" href={ingredient1}>{food1}</a></span><br/>
                        <span>{prep1}</span><br/>
                        <span><img src= {image1}/></span><br/>
                        <br></br>
                    </div>
                    <div className="food2">
                        <span><a target="_blank" href={ingredient2}>{food2}</a></span><br/>
                        <span>{prep2}</span><br/>
                        <span><img src= {image2}/></span><br/>
                        <br></br>
                    </div>
                    <div className="food3">
                        <span><a target="_blank" href={ingredient3}>{food3}</a></span><br/>
                        <span>{prep3}</span><br/>
                        <span><img src= {image3}/></span><br/>
                        <br></br>
                    </div>
                    <div className="food4">
                        <span><a target="_blank" href={ingredient4}>{food4}</a></span><br/>
                        <span>{prep4}</span><br/>
                        <span><img src= {image4}/></span><br/>
                        <br></br>
                    </div>
                    <div className="food5">
                        <span><a target="_blank" href={ingredient5}>{food5}</a></span><br/>
                        <span>{prep5}</span><br/>
                        <span><img src= {image5}/></span><br/>
                        <br></br>
                    </div>
                </div>
            }
        </div>
        );
}
