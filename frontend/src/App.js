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
      token: "",
      credentials: { username: "", password: "" },
      requestedComponent: "login",
      errors: [],
      status: "SIGNED_OUT",
      onRegistration: this.onRegistration,
      onLogin: this.onLogin,
      onSelect: this.handleMenuRequest,
      message: "",
      setMessage: this.setMessage,
      onErrors:this.onErrors,
      onBooking:this.onBooking


    }
  }

  setMessage = (msg) => {
    this.setState({ message: msg })
    setTimeout(()=>{this.setState({message:""})},5000)    

  }
  onRegistration = (next) => {
      this.setState({     
        requestedComponent: next.requestedComponent,
        message:next.message})
    }
    onBooking = (next) => {
      this.setState({     
        requestedComponent: next.requestedComponent,
        message:next.message})
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
       message:tk.message })


  }
  handleLoggout = (tk) => {
    this.setState({ token: tk.token, credentials: tk.credentials, status: tk.status })

  }

  handleMenuRequest = (rc) => {
    if (rc.requestedComponent === "log out") {
      this.setState({ status: "SIGNED_OUT" })
      this.setState({ credentials: { username: "", password: "" } })
      this.setState({ requestedComponent: "login" })
      this.setState({message:"Successfully logged out"})

    }else{
    this.setState({ requestedComponent: rc.requestedComponent })
    }
  }


  render() {
    return <>
      <div className="container">
        <Navbar {... this.state}/>
        <Controller {... this.state} />
      </div>
    </>
  }
}



export default App;
