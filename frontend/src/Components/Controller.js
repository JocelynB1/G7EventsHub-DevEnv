import React from 'react';
import LoginPage from "./LoginPage"
import SignupPage from './SignupPage';
import LandingPage from '../Pages1/LandingPage';
import BookAnEventPage from './BookAnEventPage';
import EventTable from './EventTable';

function Controller(props) {
  switch (props.requestedComponent) {
    case "login":
      return <LoginPage {... props} />

    case "register":
      return <SignupPage {... props} />

    case "home":
      return <LandingPage {...props} />

    case "book an event":
      return <BookAnEventPage {...props} />

    case "my events":
      return <EventTable {...props} />

    default:
      return <LoginPage {... props} />
      
  }

}

export default Controller;