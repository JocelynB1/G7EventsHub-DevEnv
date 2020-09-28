import React from 'react';
import Welcome from "./Welcome";
import Login from "./Login"
import SideLogo from "./SideLogo"
import "./login&signup.css"
function LoginPage(props) {
  let toSignup=()=>{
    props.onSelect({requestedComponent:"register"})
  }
  return (

    <section id="main">
      <div className="logInPage" className="Welcome">
        <div className="logo_n_para">
        <SideLogo  />
        <p>  Don't have an account? <span onClick={toSignup}  className="link"><b>Sign Up</b></span></p>

        </div>
      </div>
      <Login  {...props} />

    </section>
  )
}




export default LoginPage;