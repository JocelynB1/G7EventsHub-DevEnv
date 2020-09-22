import React from 'react';
import "./index.css";
import './main.css';
import LoginPage from "./LoginPage"
import SignupPage from './SignupPage';

function NotLoggedIn(props) {
  if (props.requestedComponent == "login") {
    return <LoginPage {... props} />

  
  } else {
    return <SignupPage {... props} />

  }
}
export default NotLoggedIn;