import React from 'react';
import Sessions from '../Components/Sessions';
import LandingNav from "../Components/LandingNav";
import SessionSideBar from '../Components/SessionSideBar';

export default function LandingPage(props) {
    return (
        <div id="landing">
          
            <div className = "landingContentent">
                <SessionSideBar/>
                <Sessions/>
             </div>
        </div>
    )
}
