import React from 'react';
import './App.css';
import "./Components/index.css";
import './Components/main.css';
import Navbar from "./Components/Navbar";
import Welcome from "./Components/Welcome";
import FormComponent from "./Components/FormComponent"
import Errors from "./Components/Errors"; 

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      details: [],
      token: "",
      credentials: { username: "", password: "" },
      requestedComponent: "login",
      errors: []

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
    //console.log(tk.errors[1])
    this.setState({ token: tk.token, credentials: tk.credentials, errors: tk.errors })
    this.loadDetails()

  }
  handleMenuRequest = (rc) => {
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
        // body: JSON.stringify(this.state.credentials)

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
          {this.state.details.map(
          user => (
            <div key={user.user}>
              <ul>
                <li>
                  {user.date_of_birth}
                </li>

                <li>
                  {user.phone_number}
                </li>

                <li>
                  {user.city}
                </li>

                <li>
                  {user.address}
                </li>

                <li>
                  {user.first_name}
                </li>

                <li>
                  {user.last_name}
                </li>

                <li>
                  {user.email}
                </li>
              </ul>
            </div>
          ))}
        <div className="container">
          <Navbar onSelect={this.handleMenuRequest} />
          {/* <Errors errors={this.state.errors}/> */}
          <br />
          <Welcome />
          <FormComponent formType={this.state.requestedComponent} onErrors={this.handleErrors} onRegistration={this.handleRegistration} onLogin={this.handleLogin} />
        </div>
        <br></br>
        {this.state.details.map(
          user => (
            <div key={user.user}>
              <ul>
                <li>
                  {user.date_of_birth}
                </li>

                <li>
                  {user.phone_number}
                </li>

                <li>
                  {user.city}
                </li>

                <li>
                  {user.address}
                </li>

                <li>
                  {user.first_name}
                </li>

                <li>
                  {user.last_name}
                </li>

                <li>
                  {user.email}
                </li>
              </ul>
            </div>
          ))}
      </>
    );
  }
}



export default App;
