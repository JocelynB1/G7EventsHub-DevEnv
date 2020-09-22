import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";
import "./index.css";
import "./index.css"


import one from "./MyImages/one.jpg";
import two from "./MyImages/two.jpg";
import three from "./MyImages/three.jpg";
import four from "./MyImages/four.jpg";
import five from "./MyImages/five.jpg";
import six from "./MyImages/six.jpg";
import seven from "./MyImages/seven.png";
import eight from "./MyImages/eight.jpg";
import nine from "./MyImages/nine.jpg";
import Event from '../Pages/Event';



export default function Listing() {
    return (
        <Router>
            <div className = "listing">
                <h1 className = "up" >UPCOMING EVENTS</h1>
                <div className = "listImage">
                <Link to ="/event" strict exact>  <img src = {one} alt = "15th June" className = "eve"/> </Link>
                <a href = "http://google.com"><img src = {two} alt = "15th June" className = "eve"/> </a>
                <a href = "http://google.com"><img src = {three} alt = "15th June" className = "eve"/> </a>
                <a href = "http://google.com"><img src = {four} alt = "15th June" className = "eve"/> </a>
                <a href = "http://google.com"><img src = {five} alt = "15th June" className = "eve"/> </a>
                <a href = "http://google.com"><img src = {six} alt = "15th June" className = "eve"/> </a>
                <a href = "http://google.com"><img src = {seven} alt = "15th June" className = "eve"/> </a>
                <a href = "http://google.com"><img src = {eight} alt = "15th June" className = "eve"/> </a>
                <a href = "http://google.com"><img src = {nine} alt = "15th June" className = "eve" /> </a>

                </div>

                <Switch>
                    <Route exact strict path="/event">
                        <Event />
                    </Route>
                </Switch>    
                
            </div>
        </Router>       
    )
} 
