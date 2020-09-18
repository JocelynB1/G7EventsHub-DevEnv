import React from 'react';
import './App.css';
import "./Components/index.css";
import './Components/main.css';
import Navbar from "./Components/Navbar";
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import LoginPage from "./Components/LoginPage"
import LogoutPage from "./Components/LogoutPage"
import Profile from './Components/Profile';
import SignupPage from './Components/SignupPage';
import BookAnEventPage from './Components/BookAnEventPage';
import { useHistory } from "react-router-dom";

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
      redirect: null


    }
  }
  
  handleRegistration = (tk) => {
    if (tk.errors) {
      this.setState({ errors: tk.errors })
    }
  }
  handleErrors = (err) => {
    if (err.errors) {
      this.setState({ errors: err.errors })
      alert(this.state.errors[0])
    }
  }
  handleLogin = (tk) => {
    this.setState({ token: tk.token, credentials: tk.credentials, errors: tk.errors, status: tk.status })
    let history = useHistory();
    history.push('/profile')

  }
  handleLoggout = (tk) => {
    this.setState({ token: tk.token, credentials: tk.credentials, status: tk.status })

  }

  handleMenuRequest = (rc) => {
    if (rc.requestedComponent === "log out") {
      this.setState({ status: "SIGNED_OUT" })
      this.setState({ credentials: { username: "", password: "" } })
      this.setState({ requestedComponent: "login" })

    }
    this.setState({ requestedComponent: rc.requestedComponent })
  }
  render() {
    
    if (this.state.token === "") {
      return (
        <>
          <Router>
            <div className="container">
              <Navbar
                token={this.state.token}
                onSelect={this.handleMenuRequest}
                status={this.state.status}
                requestedComponent={this.state.requestedComponent}
              />

              <Switch>
                <Route path="/" exact render={props => <LoginPage {...props} onErrors={this.handleErrors} onLogin={this.handleLogin} />} />
                <Route path="/login" exact render={props => <LoginPage {...props} onErrors={this.handleErrors} onLogin={this.handleLogin} />} />
                <Route path="/register" exact render={props => <SignupPage {...props} token={this.state.token}  onRegistration={this.handleRegistration} onErrors={this.handleErrors} />} />

                {/* <Main
            details={this.state.details}
            requestedComponent={this.state.requestedComponent}
            onErrors={this.handleErrors}
            onRegistration={this.handleRegistration}
            onLogin={this.handleLogin}
          /> */}
              </Switch>
            </div>
          </Router>
        </>
      );
    } else {
      return (
        <>
          <Router>
            <div className="container">
              <Navbar
                token={this.state.token}
                onSelect={this.handleMenuRequest}
                status={this.state.status}
                requestedComponent={this.state.requestedComponent}
              />

              <Switch>
                <Route path="/logout" exact render={props => <LogoutPage {...props} onLogout={this.handleLoggout} />} />
                <Route path="/" exact render={props => <Profile {...props} token={this.state.token} details={this.state.details} />} />
                <Route path="/bookAnEvent" exact render={props => <BookAnEventPage {...props} onErrors={this.handleErrors} token={this.state.token} />} />

                {/* <Main
                  details={this.state.details}
                  requestedComponent={this.state.requestedComponent}
                  onErrors={this.handleErrors}
                  onRegistration={this.handleRegistration}
                  onLogin={this.handleLogin}
                /> */}
              </Switch>
            </div>
          </Router>
        </>
      );

    }
  }
}



export default App;
