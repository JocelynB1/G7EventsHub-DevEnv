import React from 'react';
import Welcome from "./Welcome";
import Login from "./Login"

function LoginPage(props) {
            return (
            
                <section id="main">
                  <Welcome />
                  <Login formType={props.requestedComponent} onErrors={props.onErrors}
                   onLogin={props.onLogin}  />
                </section>
               )
        }
        
        
    

export default LoginPage;