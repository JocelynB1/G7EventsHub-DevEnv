import React from 'react';
import './landing.css';
import Events from "./MorningEvents"


export default function MorningSide(props) {
    // <a href = "/"><b>See more events....</b></a>
   
    return (
      <>
        <div className = "morning" >
            <h1>Morning Events</h1>
            <Events {... props} />
        </div>
        </>
    )
}
