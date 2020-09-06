import React from 'react';
import "./index.css";
import Login from "./Login";
import Form from './Form';


function FormComponent(props) {
    const formType = props.formType;
    if (formType==="login") {
    return <Login onLogin={props.onLogin}/>;
    
    }
    return <Form />;
  }
  
  export default FormComponent;