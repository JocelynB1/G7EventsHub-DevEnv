import React from 'react';
import "./index.css";

export default class Football extends React.Component {
    msg() {
      alert("Thank you for registering for the event");
    }
    render() {
       
        return (
                  <button className = "btn" onClick = {this.msg}>Register</button>
                );
    }
}
