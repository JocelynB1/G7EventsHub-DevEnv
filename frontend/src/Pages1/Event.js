import React from 'react'
import Speaker from '../Components/Speaker'
import EventDetails from '../Components/EventDetails';
import "../Components/index.css";
import LandingNav from '../Components/LandingNav';

export default function Event() {
    return (
        <div className = "event">
            <LandingNav/>
            <div className = "details"> 
            <Speaker/>
            <EventDetails/>
            </div>
            
        </div>
    )
}
