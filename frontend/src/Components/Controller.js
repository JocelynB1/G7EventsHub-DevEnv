import React from 'react';
import NotLoggedIn from './NotLogedInPage';
import LandingPage from '../Pages1/LandingPage';
import BookAnEventPage from './BookAnEventPage';
import EventTable from './EventTable';

function Controller(props) {
  switch (props.requestedComponent) {
    case "login":
    case "register":
      return <NotLoggedIn {...props} />
      break;

    case "home":
      return <LandingPage {...props} />
      break;
    case "book an event":
      return <BookAnEventPage {...props} />
      break;
    case "my events":
      return <EventTable {...props} />
      break;
      
    default:
      break;
  }

}

export default Controller;