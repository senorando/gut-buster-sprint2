import * as React from 'react';
import { Socket } from './Socket';
import SearchField from "react-search-field";
 
export function FoodSearch() {
    function handleSubmit(response) {
        console.log(response);
        let name = response;
        Socket.emit('new search', {
          'search': name,
       });
       console.log('Sent the food ' + name + ' to server!');
    }
    
        
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
