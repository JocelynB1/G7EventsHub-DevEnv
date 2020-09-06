import React from 'react';


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
            data=>data.json()
        )
        .then(
            data => this.props.onLogin({token:data.token,credentials:this.state.credentials})

        ).catch(error => console.log(error))
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
                    <button onClick={this.postLogin} className="button"  type="submit">Login</button>
                </form>
                </div>
            </>
        );
    }
}
export default Login;