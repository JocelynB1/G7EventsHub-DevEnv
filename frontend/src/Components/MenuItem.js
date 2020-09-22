import React from 'react';

class MenuItem extends React.Component{
    onSelect = (event) => {
        event.preventDefault();
        this.props.onSelect({requestedComponent:this.props.menulabel})
     }
    render(){
        return(<li className = "menuListItem" onClick={this.onSelect}>{this.props.menulabel}</li>)
    }
}
export default MenuItem;