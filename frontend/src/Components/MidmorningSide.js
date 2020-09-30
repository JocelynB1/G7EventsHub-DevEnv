import React from 'react';
import './landing.css';
import Events from "./MidmorningEvents"


export default function MidmorningSide(props) {
    return (
      <>
        
        <div className = "morning" >
            <h1>Midmorning Events</h1>
            <Events {... props} />
        </div>
        
        </>
    )
}
