import * as React from 'react';
import { Socket } from './Socket';
import SearchField from "react-search-field";
 
export function FoodSearch() {
    function handleSubmit(response) {
        console.log(response);
        let name = response;
        Socket.emit('new food search', {
          'food_search': name,
       });
       console.log('Sent the food ' + name + ' to server!');
    }
    
    function getfoodresponse() {
        React.useEffect(() => {
            Socket.on('food response', (data) => {
                console.log("Received addresses from server for food_name: " + data['name']);
             
            })
        });
    }
   
   getfoodresponse();
        
    return (
         <div>
            <div>Food Search</div>
            <SearchField
                  placeholder="Search..."
                  classNames="test-class"
                  onSearchClick={handleSubmit}
                />
        </div>
        
        );
}
