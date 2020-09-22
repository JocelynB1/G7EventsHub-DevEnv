import React from 'react';
import MenuItem from "./MenuItem"

class MenuOptions extends React.Component {
    constructor(props) {
    super(props);
        this.state = {
            details: [],
            token: "",
            credentials: { username: "", password: "" },
            status: {
                SIGNED_OUT: ["register", "login"],
                ATTENDEE_SIGNED_IN: ["home","book an event","my events","log out"],
                SPEAKER_SIGNED_IN: []

            }

        }
    }

    render() {
        let status=this.state.status[this.props.status]
        return (
            status.map(
                option => {
                    
                    return (<MenuItem key={option} onSelect={this.props.onSelect} menulabel={option} />)
                }
            )
        )
    }
}
export default MenuOptions;