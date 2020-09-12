import React from 'react';
import './Navbar.css';
import MenuItem from "./MenuItem"

class MenuOptions extends React.Component {
    constructor(props) {
    super(props);
        this.state = {
            details: [],
            token: "",
            credentials: { username: "", password: "" },
            requestedComponent: "login",
            status: {
                SIGNED_OUT: ["register", "login"],
                ATTENDEE_SIGNED_IN: ["profile","log out"],
                SPEAKER_SIGNED_IN: []

            }

        }
    }
    render() {
        return (
            this.state.status[this.props.status].map(
                option => {
                    return (<MenuItem key={option} onSelect={this.props.onSelect} menulabel={option} />)
                }
            )
        )
    }
}
export default MenuOptions;