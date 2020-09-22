import React from 'react';
//import ReactDom from "react-dom";
import "./index.css";
import Button from "./Button"


export default function EventDetails() {
    return (
        <div className = "eventDetails">
            <div className = "table">
                <h1>Event Details</h1>
                    <ul>
                        <li>Event Name:   Girl-Tech Power</li>
                        <li>Date:    14th July, 2020   </li>
                        <li>Topic: Girls Takng over </li>
                        <li>Session:   Morning </li>
                        <li>Speaker(s):   Regina Honu </li>
                        <li>Room Capacity: 45 </li>
                    </ul>

               
            </div>
            <Button/>
            {/* <button className = "btn">Register</button> */}
        </div>
    )
}
