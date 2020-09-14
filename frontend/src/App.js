import React from 'react';
import './App.css';
import "./Components/index.css";
import './Components/main.css';
import Navbar from "./Components/Navbar";
import Main from "./Components/Main"
class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      details: [],
      token: "",
      credentials: { username: "", password: "" },
      requestedComponent: "login",
      errors: [],
      status: "SIGNED_OUT"

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
    this.setState({ token: tk.token, credentials: tk.credentials, errors: tk.errors, status: tk.status, requestedComponent: tk.requestedComponent })
    this.loadDetails()

  }
  handleMenuRequest = (rc) => {
    if (rc.requestedComponent === "log out") {
      this.setState({ status: "SIGNED_OUT" })
      this.setState({ credentials: { username: "", password: "" } })
      this.setState({ requestedComponent: "login" })
    
    }
    this.setState({ requestedComponent: rc.requestedComponent })
  }
  loadDetails() {

    fetch("http://127.0.0.1:8000/api/details/",
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${this.state.token}`
        },

      }
    ).then(
      data => data.json()

    ).then(
      data => this.setState({ details: data }),
    )
      .then(

      ).catch(error => console.log(error))

  }
  render() {
    return (
      <>

        <div className="container">
          <Navbar onSelect={this.handleMenuRequest}
            status={this.state.status}
            requestedComponent={this.state.requestedComponent}
          />
          {/* <Errors errors={this.state.errors}/> */}
          <br />
          <Main
            details={this.state.details}
            requestedComponent={this.state.requestedComponent}
            onErrors={this.handleErrors}
            onRegistration={this.handleRegistration}
            onLogin={this.handleLogin}
          />
        </div>
        <br></br>

      </>
    );
  }
}



export default App;
