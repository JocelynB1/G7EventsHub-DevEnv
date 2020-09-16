import React from 'react';
import './Navbar.css';
import Welcome from "./Welcome";
import Login from "./Login"

class LoginPage extends React.Component {
    constructor(props) {
    super(props);
     
    }
    render() {
            return (
            
                <section id="main">
                  <Welcome />
                  <Login formType={this.props.requestedComponent} onErrors={this.props.onErrors}
                   onLogin={this.props.onLogin}  />
                </section>
               )
        }
        
        
    }

export default LoginPage;