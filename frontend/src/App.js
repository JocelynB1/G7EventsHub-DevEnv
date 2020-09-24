import React from 'react';
import './App.css';
import "./Components/index.css";
import './Components/main.css';
import './Components/Navbar.css';

import Navbar from "./Components/Navbar";
import Controller from './Components/Controller';
class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      details: [],
      token: null,
      credentials: { username: "", password: "" },
      requestedComponent: null,
      errors: [],
      status: "SIGNED_OUT",
      onSuccess: this.onSuccess,
      onLogin: this.onLogin,
      onSelect: this.handleMenuRequest,
      message: "",
      setMessage: this.setMessage,
      onErrors: this.onErrors


    }

  }

  setMessage = (msg) => {
    this.setState({ message: msg })

  }
  onSuccess = (next) => {
  
    this.setState({
      requestedComponent: next.requestedComponent,
      message: next.message
    })
  }
  onFailure = (next) => {
   
    this.setState({
      message: next.message
    })
  }

  onErrors = (err) => {
    if (err.errors) {
      this.setState({ errors: err.errors })
      alert(this.state.errors[0])
    }
  }
  onLogin = (tk) => {
    this.setState({
      token: tk.token,
      credentials: tk.credentials,
      errors: tk.errors,
      status: tk.status,
      requestedComponent: tk.requestedComponent,
      message: tk.message
    })
    window.localStorage.setItem("token", tk.token)

  }

  handleMenuRequest = (rc) => {
    if (rc.requestedComponent === "log out") {
      this.setState({ status: "SIGNED_OUT" })
      this.setState({ credentials: { username: "", password: "" } })
      this.setState({ requestedComponent: "login" })
      this.setState({ message: "Successfully logged out" })
      localStorage.clear()

    } else {
      this.setState({ requestedComponent: rc.requestedComponent })
    }
  }


  render() {
    if (window.localStorage.hasOwnProperty("token") && this.state.token === null) {
      this.setState({ token: window.localStorage.getItem("token") })
      this.setState({ status: "ATTENDEE_SIGNED_IN" })
      this.setState({ message: "Welcome back" })
      this.setState({ requestedComponent: "home" })
    }
    return <>
      <div className="container">
        <Navbar {... this.state} />
        <Controller {... this.state} />
      </div>
    </>
  }
}



export default App;
