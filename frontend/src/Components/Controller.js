import React from 'react';
import LoginPage from "./LoginPage"
import SignupPage from './SignupPage';
import LandingPage from '../Pages1/LandingPage';
import BookAnEventPage from './BookAnEventPage';
import EventTable from './EventTable';
import Navbar from './Navbar';
import Footer from './Footer';
function Controller(props) {
  switch (props.requestedComponent) {
    case "login":
      return <LoginPage {... props} />

    case "register":
      return <SignupPage {... props} />

    case "Home":
      return <>
      <Navbar {...props} />
      <LandingPage {...props} />
      <Footer/>
      </>

    case "book an event":
      return <>
      <Navbar {...props} />
      <BookAnEventPage {...props} />
      <Footer/>
      </>
    case "My events":
      return<>
      <Navbar {...props} />
      <EventTable {...props} />
      <Footer/>
      </>
    default:
      return <LoginPage {... props} />
      
  }

}

export default Controller;