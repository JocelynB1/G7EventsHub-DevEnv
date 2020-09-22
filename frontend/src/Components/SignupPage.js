import React from 'react';
import Welcome from "./Welcome";
import Form from "./Form"

class LoginPage extends React.Component {
    constructor(props) {
    super(props);
     
    }
    render() {
            return (
            
                <section id="main">
                  <Welcome />
                  <Form formType={this.props.requestedComponent} onErrors={this.props.onErrors}
                   onSuccess={this.props.onSuccess}  />
                </section>
               )
        }
        
        
    }

export default LoginPage;