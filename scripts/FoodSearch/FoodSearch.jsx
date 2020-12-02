import React, { useState, useEffect } from 'react';
import { UserForm } from '../UserForm';
import { Socket } from '../Socket';
import { RatingStar } from '../StarRating';
import SearchField from "react-search-field";

export function FoodSearch(props) {
    const isLoggingIn = props.isLoggingIn;
    const isLoggedIn = props.currentUser.isLoggedIn;
    const currentUser = props.currentUser;
    
    function onClickAlert(){
        alert("Please Login");
    }
    
    function handleSubmit(response) {
        console.log(response);
        let name = response;
        let user = currentUser.email;
        Socket.emit('new food search', {
          'food_search': name,
          'user': user
        });
       console.log('Sent the food ' + name + user + ' to server!');
    }
    
    const [food, setFoods] = useState([]);
    const [ingredient, setIngredient] = useState([]);
    const [prep, setPrep] = useState([]);
    const [image, setImage] = useState([]);
    const [calorie, setCalorie] = useState([]);
    
    
    const [food1, setFoods1] = useState([]);
    const [ingredient1, setIngredient1] = useState([]);
    const [prep1, setPrep1] = useState([]);
    const [image1, setImage1] = useState([]);
    const [calorie1, setCalorie1] = useState([]);
    
    const [food2, setFoods2] = useState([]);
    const [ingredient2, setIngredient2] = useState([]);
    const [prep2, setPrep2] = useState([]);
    const [image2, setImage2] = useState([]);
    const [calorie2, setCalorie2] = useState([]);
    
    const [food3, setFoods3] = useState([]);
    const [ingredient3, setIngredient3] = useState([]);
    const [prep3, setPrep3] = useState([]);
    const [image3, setImage3] = useState([]);
    const [calorie3, setCalorie3] = useState([]);
    
    const [food4, setFoods4] = useState([]);
    const [ingredient4, setIngredient4] = useState([]);
    const [prep4, setPrep4] = useState([]);
    const [image4, setImage4] = useState([]);
    const [calorie4, setCalorie4] = useState([]);
   
    const [food5, setFoods5] = useState([]);
    const [ingredient5, setIngredient5] = useState([]);
    const [prep5, setPrep5] = useState([]);
    const [image5, setImage5] = useState([]);   
    const [calorie5, setCalorie5] = useState([]);

    function GetFoodResponse() {
        useEffect(() => {
            Socket.on('food response', (data) => {
                setFoods(data[0][0]);
                setPrep(data[0][1] + " minutes prep time");
                setIngredient(data[0][2]);
                setImage(data[0][3]);
                setCalorie(data[0][4] + " calories");

                setFoods1(data[1][0]);
                setPrep1(data[1][1] + " minutes prep time");
                setIngredient1(data[1][2]);
                setImage1(data[1][3]);
                setCalorie1(data[1][4] + " calories");
                
                setFoods2(data[2][0]);
                setPrep2(data[2][1] + " minutes prep time");
                setIngredient2(data[2][2]);
                setImage2(data[2][3]);
                setCalorie2(data[2][4] + " calories");
                
                setFoods3(data[3][0]);
                setPrep3(data[3][1] + " minutes prep time");
                setIngredient3(data[3][2]);
                setImage3(data[3][3]);
                setCalorie3(data[3][4] + " calories");
                
                setFoods4(data[4][0]);
                setPrep4(data[4][1] + " minutes prep time");
                setIngredient4(data[4][2]);
                setImage4(data[4][3]);
                setCalorie4(data[4][4] + " calories");
                
                setFoods5(data[5][0]);
                setPrep5(data[5][1] + " minutes prep time");
                setIngredient5(data[5][2]);
                setImage5(data[5][3]);
                setCalorie5(data[5][4] + " calories");
                
            });
            Socket.off('food response', '');
        }, []);
    }
   
   GetFoodResponse();
   
   
        
    return (
         <div id = 'FoodSearch'>
            <img src={'../static/eat-right.png'} alt="Logo"
                style={{float: 'right',
                        position: 'relative',
                        top: 150
                        }}
            />
            { isLoggingIn?
                <div id = 'UserForm'>
                    <UserForm />
                </div>
                :
                <div id = 'SearchContent'>
                    <h3>Food Search</h3>
                    { isLoggedIn?
                        <div>
                            <SearchField
                                  placeholder="Search..."
                                  classNames="test-class"
                                  onSearchClick={handleSubmit}
                                /><br/>
                            <br/>
                            <div className="food">
                                <span><a target="_blank" href={ingredient}>{food}</a></span><br/>
                                <span>{calorie}</span><br/>
                                <span>{prep}</span><br/>
                                <span><img src= {image}/></span><br/>
                                <br></br>
                            </div>
                            <div className="food1">
                                <span><a target="_blank" href={ingredient1}>{food1}</a></span><br/>
                                <span>{calorie1}</span><br/>
                                <span>{prep1}</span><br/>
                                <span><img src= {image1}/></span><br/>
                                <br></br>
                            </div>
                            <div className="food2">
                                <span><a target="_blank" href={ingredient2}>{food2}</a></span><br/>
                                <span>{calorie2}</span><br/>
                                <span>{prep2}</span><br/>
                                <span><img src= {image2}/></span><br/>
                                <br></br>
                            </div>
                            <div className="food3">
                                <span><a target="_blank" href={ingredient3}>{food3}</a></span><br/>
                                <span>{calorie3}</span><br/>
                                <span>{prep3}</span><br/>
                                <span><img src= {image3}/></span><br/>
                                <br></br>
                            </div>
                            <div className="food4">
                                <span><a target="_blank" href={ingredient4}>{food4}</a></span><br/>
                                <span>{calorie4}</span><br/>
                                <span>{prep4}</span><br/>
                                <span><img src= {image4}/></span><br/>
                                <br></br>
                            </div>
                            <div className="food5">
                                <span><a target="_blank" href={ingredient5}>{food5}</a></span><br/>
                                <span>{calorie5}</span><br/>
                                <span>{prep5}</span><br/>
                                <span><img src= {image5}/></span><br/>
                                <br></br>
                            </div>
                        </div>
                        :
                        <div>
                            <SearchField
                                  placeholder="please login to search..."
                                  classNames="test-class"
                                  onSearchClick={onClickAlert}
                                /><br/>
                        </div>
                    }
                </div>
            }
        </div>
        );
}
