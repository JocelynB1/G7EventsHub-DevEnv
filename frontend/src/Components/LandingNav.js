import React from 'react';
import navLogo from "./navLogo.png";
// import "./index.css";

export default function LandingNav() {
    return (
        <div className = "landingNav" >
            <nav className = "menu">
                <div className = "logoDiv">
                    <img src={navLogo} className="navLogo" alt="logo" />
                </div>

                <div className= "menuDiv">
                    <ul className = "menuList">
                        <li className = "menuListItem"> <a className = "menuLink" href = "/">Home </a></li>
                        <li className = "menuListItem"> <a className = "menuLink" href = "https://google.com"> My Events</a> </li>
                        <li className = "menuListItem"> <a className = "menuLink" href = "/"> About</a> </li>
                        <li className = "menuListItem"> <a className = "menuLink" href = "/">Contact </a></li>
                    </ul>
                </div>

            </nav>
        </div>

    )
}
