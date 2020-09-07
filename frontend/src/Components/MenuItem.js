import React from 'react';

class MenuItem extends React.Component{
    onSelect = (event) => {
        event.preventDefault();
        this.props.onSelect({requestedComponent:this.props.menulabel})
     }
    render(){
        return(
            <>
             <a href="#" onClick={this.onSelect}>{this.props.menulabel}</a>
            </>)
    }
}
export default MenuItem;