import React from 'react';
import Sessions from '../Components/Sessions';
import LandingNav from "../Components/LandingNav";
import SessionSideBar from '../Components/SessionSideBar';
import "../Components/landing.css"
export default function LandingPage(props) {
    return (
        <div id="landing">
          
            <div className = "landingContentent">
                <Sessions  {...props} />
             </div>
        </div>
    )
}
