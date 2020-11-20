import * as React from 'react';

import { UserForm } from './userForm';
import { Socket } from './Socket';
import SearchField from "react-search-field";

export function FoodSearch(props) {
    const isLoggingIn = props.isLoggingIn;
    
    function handleSubmit(response) {
        console.log(response);
        let name = response;
        Socket.emit('new food search', {
          'food_search': name,
       });
       console.log('Sent the food ' + name + ' to server!');
    }
    
    const [food, setFoods] = React.useState([]);
    const [ingredient, setIngredient] = React.useState([]);
    const [prep, setPrep] = React.useState([]);
    const [image, setImage] = React.useState([]);
    const [calorie, setCalorie] = React.useState([]);

    function GetFoodResponse() {
        React.useEffect(() => {
            Socket.on('food response', (data) => {
                //console.log("Received addresses from server for food_name: " + data['name']);
                let food_name = data['name'];
                console.log(food_name);
                setFoods(data['name']);
                setIngredient(data['recepie_list']);
                setPrep(data['preptime'] + " minutes prep time");
                setImage(data['image_url']);
                setCalorie(data['calories'] + " calories");
        });
    });
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
                        />
                    <span>{food}</span>
                    <span>{calorie}</span>
                    <span>{prep}</span>
                    <img src= {image}/>
                    <ol>
                        {
                            ingredient.map((ingredient, index) =>
                            <dt key={index}>{ingredient}</dt>)
                        }
                    </ol>
                </div>
            }
        </div>
        );
}
