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
                ATTENDEE_SIGNED_IN: ["Home","My events","Sign Out"],
                SPEAKER_SIGNED_IN: []

            }

        }
    }

    render() {
        let status=this.state.status[this.props.status]
        let newMenu=[]
        //Remove seleted element
        status.forEach(element => {
            if(element!==this.props.requestedComponent){
                newMenu.push(element)
            }
        });
        return (
            newMenu.map(
                option => {
                    
                    return (<MenuItem key={option} onSelect={this.props.onSelect} menulabel={option} />)
                }
            )
        )
    }
}
export default MenuOptions;