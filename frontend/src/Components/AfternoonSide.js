import React from 'react';
import './landing.css';
import Events from "./AfternoonEvents"


export default function AfternoonSide(props) {
    return (
      <>
    
        <div className = "morning" >
            <h1>Afternoon Events</h1>
            <Events {... props} />
        </div>
    
        </>
    )
}
