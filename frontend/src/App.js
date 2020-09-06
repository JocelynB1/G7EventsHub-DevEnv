import React from 'react';
import './App.css';
import './Components/main.css';
import Navbar from "./Components/Navbar";
import Welcome from "./Components/Welcome";
import FormComponent from "./Components/FormComponent"
class App extends React.Component{
  constructor(props) {
    super(props);
    this.state={
      details:[],
      token:"",
        credentials: { username: "", password: "" },
        requestedComponent:"login"

    
    }
 }

 handleLogin=(tk)=>{
   console.log(tk)
    this.setState({token:tk.token,credentials:tk.credentials })
      this.loadDetails()

 }
  loadDetails(){

        fetch("http://127.0.0.1:8000/api/details/",
            {
                method: "GET",
                 headers: { "Content-Type": "application/json" ,
                 Authorization:`Token ${this.state.token}`},
                // body: JSON.stringify(this.state.credentials)
                
            }
        ).then(
          data=>data.json()
           
        ).then(
          data=>this.setState({details:data}),
      )
        .then(

        ).catch(error => console.log(error))
        
  }
   render(){
    return(
      <>
      <div className="container">
      <Navbar/>
      <br/>
      <Welcome/>
      <FormComponent formType={this.state.requestedComponent} onLogin={this.handleLogin} />
      </div>
      <br></br>
        { this.state.details.map(
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
