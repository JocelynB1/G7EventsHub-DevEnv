import React from 'react';
import './App.css';
import axios from "axios";
import Login from "./Components/Login";
import Navbar from "./Components/Navbar";
import Welcome from "./Components/Welcome";
import Form from'./Components/Form';
class App extends React.Component{
  constructor(props) {
    super(props);
    this.state={
      details:[],
      token:"",
        credentials: { username: "", password: "" }
    
    }
 }

 handleLogin=(tk)=>{
   console.log(tk)
    this.setState({token:tk.token,credentials:tk.credentials })
      this.loadDetails()

 }
  // state={
  //   details:[]
  // };

  // componentDidMount(){
  //   this.getDetails();
  // }

  // getDetails(){
  //   // axios
  //   // .get("http://127.0.0.1:8000/api/")
  //   // .then(res=>{
  //   //   this.setState({details:res.data});
  //   // })
  //   // .catch(err=>{
  //   //   console.log(err);
  //   // });
  // }
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
      <Navbar/>
      <Welcome/>
      <Form/>
      <br></br>
        <Login onLogin={this.handleLogin}/>
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
