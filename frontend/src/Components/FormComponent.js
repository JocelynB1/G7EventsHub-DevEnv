import React from 'react';
import "./index.css";
import Login from "./Login";
import Form from './Form';


function FormComponent(props) {
  const formType = props.formType;
  if (formType === "login") {
    return <Login errors={props.errors} onLogin={props.onLogin} />;
  }
  if (formType === "register") {
    return <Form errors={props.errors}/>;
  }
}

export default FormComponent;