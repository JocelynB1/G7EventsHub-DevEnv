import React from 'react';
import Errors from "./Errors"; 


class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            credentials: { username: "", password: "" }
        }
    }
    postLogin = (event) => {
        event.preventDefault();

        fetch("http://127.0.0.1:8000/auth/",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(this.state.credentials)
            }
        ).then(

            //400
            data => {

                if (!data.ok) {
                    //         console.log(data.text())
                    data.json().then((err) => {
                        let errorArr = []
                        Object.keys(err).map(key =>
                            errorArr.push(key+" : "+ err[key].pop())
                        )
                        this.props.onLogin({ token: "", credentials: "", errors: errorArr })

                    });
                } else {
                    data.json().then(
                        data => {
                            console.log(data)

                            this.props.onLogin({ token: data.token, credentials: this.state.credentials, errors: [] })
                        }

                    ).catch(error => console.log(error)
                        // this.props.onLogin({token:"abc",credentials:this.state.credentials,errors:error.text})
                    )
                }
            }
        )

    }
    handleChange = (event) => {
        const cred = this.state.credentials
        cred[event.target.name] = event.target.value
        this.setState({ credentials: cred });
    }
    render() {
        return (
            <>
                <div className="form">
      <Errors errors={this.props.errors}/>

                    <form method="post">
                        <h2>Login</h2>

                        <p>
                            <label htmlFor="id_username">Username:</label>
                            <input type="text" name="username" autoFocus autoCapitalize="none" autoComplete="username" maxLength="150" required id="id_username"
                                value={this.state.credentials.username} onChange={this.handleChange} />
                        </p>
                        <p><label htmlFor="id_password">Password:</label>
                            <input type="password" name="password" autoComplete="current-password" required id="id_password"
                                value={this.state.credentials.password} onChange={this.handleChange} />
                        </p>
                        <button onClick={this.postLogin} className="button" type="submit">Login</button>
                    </form>
                </div>
            </>
        );
    }
}
export default Login;