import React from 'react';
import Welcome from "./Welcome";
import Form from "./Form"
import "./login&signup.css"
import SideLogo from "./SideLogo"

class SignupPage extends React.Component {
  constructor(props) {
    super(props);

  }
   toLogin=()=>{
    this.props.onSelect({requestedComponent:"login"})
  }
  
  render() {
    return (

      <section id="main">
        <div className="signUpPage"  className="Welcome">
          <div className="logo_n_para">
            <SideLogo />
            <p>Already have an account? <span onClick={this.toLogin} className="link"><b>Login</b></span></p>
          </div>
        </div>

        <Form  {...this.props} />
      </section>
    )
  }


}

export default SignupPage;