// importing react & logo(image)
import React from 'react';
// import logo from "./logo.png";
import logo from "./img/logo.svg";

const Welcome = () => {
    return (
        <div className = "Welcome">
            
            <img src={logo} className="Welcomelogo" alt="logo" /><br/>
            {/* <h1>Welcome to Events and more</h1>
            Register for the Event of your choice with just a few clicks.<br/>
            <h2>ENJOY!!! </h2>  */}
        </div>
    )
};

export default Welcome;
