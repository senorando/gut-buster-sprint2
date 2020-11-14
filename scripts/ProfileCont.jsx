import React, { useState, useEffect } from 'react';

import { UpdateForm } from './UpdateForm';
import { Socket } from './Socket';

export function ProfileCont(props){
    const currentUser = props.currentUser;
    const [isEdit, setStatus] = useState(false);
    const profileDetail = props.profileDetail;
    function updateStatus() {
        setStatus((prevStatus) => !isEdit);
    }
    return (
        <div>
            <h1> { currentUser.name } </h1><br/>
            <label>Height: { profileDetail.height }</label><br/>
            <label>Age:{ profileDetail.age }</label><br/>
            <label>Gender:{ profileDetail.gender }</label><br/>
            <label>Activity Level:{ profileDetail.activityLevel }</label><br/>
            <label>Estimated Weight Gain: </label><br/>
            { isEdit? 
                <div id = 'UserForm'>
                    <UpdateForm />
                </div>
                :
                <button onClick = { updateStatus }>Edit</button>
            }
        </div>
    )
}