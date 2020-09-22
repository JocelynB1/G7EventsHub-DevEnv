import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";
import "./index.css";
import EventListing from '../Pages1/EventListing';

export default function Sessions() {
    return (
        <Router>   

                <div className= "button">

                    <h1>Please Choose Your Preferred Event Session</h1>
                  <Link to = "/eventlisting">  <button>MORNING</button> <br/></Link>
                  <Link to = "">  <button>AFTERNOON</button> <br/> </Link>
                  <Link to = ""> <button>EVENING</button> <br/></Link>

                </div>

            <Switch>
            <Route exact strict path="/eventlisting">
            <EventListing />
          </Route>
            </Switch>    
        </Router>         
    )
}
