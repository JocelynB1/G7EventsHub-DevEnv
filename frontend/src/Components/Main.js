import React from 'react';
import Welcome from "./Welcome";
import FormComponent from "./FormComponent"
import Profile from './Profile';

class MenuOptions extends React.Component {
    constructor(props) {
    super(props);
        this.state = {
            details: [],
            token: "",
            credentials: { username: "", password: "" },
            requestedComponent: "login",
            status: {
                SIGNED_OUT: ["register", "login"],
                ATTENDEE_SIGNED_IN: ["profile","log out"],
                SPEAKER_SIGNED_IN: []

            }

        }
    }
    render() {
        if(this.props.requestedComponent=="login"||this.props.requestedComponent=="register"){
            return (
            
                <section id="main">
                  <Welcome />
                  <FormComponent formType={this.props.requestedComponent} onErrors={this.props.onErrors}
                   onSuccess={this.props.onSuccess} onLogin={this.props.onLogin}  />
                </section>
               )
        }
        else{
            return (
               
                <section id="main">
                <Profile details={this.props.details}/>
                </section> 
            )
        }
        
    }
}
export default MenuOptions;