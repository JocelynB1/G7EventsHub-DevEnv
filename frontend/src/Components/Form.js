// importing react & css
import React from 'react';

function Form(props) {
   let postSignUp =async  (event) => {
        event.preventDefault();
        const formData = new FormData(document.querySelector("#form"))
        formData.append("first_name", document.querySelector("#first_name").value)
        formData.append("password", document.querySelector("#password").value)
        formData.append("confirm_password", document.querySelector("#confirm_password").value)
        formData.append("last_name", document.querySelector("#last_name").value)
        formData.append("username", document.querySelector("#username").value)
        formData.append("phone_number", document.querySelector("#phone_number").value)
        formData.append("email", document.querySelector("#email").value)
        formData.append("confirm_email", document.querySelector("#confirm_email").value)
        formData.append("password", document.querySelector("#password").value)
        formData.append("date_of_birth", document.querySelector("#date_of_birth").value)
        formData.append("city", document.querySelector("#city").value)
       let data =await fetch("http://127.0.0.1:8000/api/register/",
        {
            method: "POST",
            body: formData
        })
        try{
            if(data.status==200){
                props.onSuccess({
                    requestedComponent:"login",
                    message:"Registration succesful please sign in"
                })

            }
            if (!data.ok) {
                let err = await data.json()
                    let errorArr = []
                    Object.keys(err).map(key =>
                        errorArr.push(key + " : " + err[key])
                    )
                    props.onErrors({ errors: errorArr })
                    // props.onFailure({message:errorArr})
             
            } else {
                let d = await data.json()
                props.onSuccess({
                    requestedComponent:"login",
                    message:"Registration succesful please sign in"
                })
            }
            
                
            
        } catch(error){
            props.onErrors({ errors: error.text })
            // props.onFailure({message:error.text})

     }
    
     }

        return (
            <div className="form" className="signUpForm" >

                {/* craeting input fields for the sign up form */}
                <form id="form">

                    <h2>Sign Up Here</h2>

                    {/* <label>Firstname :</label> */}
                    <input type="text" required placeholder="First Name *" id="first_name" className="firstName"  width="50%"  ></input>
                    {/* <label>Lastname :</label> */}
                    <input type="text" required placeholder="Last Name *" id="last_name"  width="50%" className="lastName" />
                    <br />
                    {/* <label>Username :</label> */}
                    <input type="text" required placeholder="Username *" id="username" className="username" />
                    <input type="tel" required placeholder="Phone Number *" id="phone_number" className="phone" /><br />
                    {/* <label>Email :</label> */}


                    <input type="password" required placeholder="Password *" id="password" className="password" />

                    <input type="password" required placeholder="Confirm Password *" id="confirm_password" className="confirmPassword" /><br />
                   
                    <input type="date" required placeholder="Date of birth*" id="date_of_birth" className="date_of_birth"  height="25%" width="200%" />
                   
                    {/* <label>City :</label> */}
                    <input type="text" required placeholder="City *" id="city" className="city" height="25%" width="100%"  ></input>
                    {/* <label>Lastname :</label> */}
                    <br />
                    <input type="email" required placeholder="Email *" id="email" className="email" />
                    <input type="email" required placeholder="Confirm Email *" id="confirm_email" className="confirm_email" />

                    <br />

                    <button type="submit" onClick={postSignUp}  value="Sign Up" >Sign Up</button>

                </form>

            </div>
        )

    }


export default Form