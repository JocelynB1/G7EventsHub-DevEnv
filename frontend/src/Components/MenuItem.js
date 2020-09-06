import React from 'react';
import './App.css';

class MenuItem extends React.Component{

    constructor(props) {
        super(props);
        this.state={
        }
     }
     postLogin = (event) => {
        event.preventDefault();
        this.props.checkMenu({requestedComponent:this.props.menulabel})
     }
    render(){
            <>
             <a href="#" onClick={this.checkMenu}>{this.props.menulabel}</a>
            </>
    }
}
export default MenuItem;