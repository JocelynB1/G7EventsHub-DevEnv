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
                  <Form  {...this.props}  />
                </section>
               )
        }
        
        
    }

export default LoginPage;