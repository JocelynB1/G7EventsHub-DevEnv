import React from 'react';
import './Navbar.css';
import menuLogo from "./img/logo.svg"
import MenuItem from "./MenuItem"

class Navbar extends React.Component{

   render(){
        return(
            <nav className="menu">
            <div className="logo1">
                <img src={menuLogo} alt="" srcSet="" id="pic_logo" />
            </div>
            <MenuItem onSelect={this.props.onSelect} menulabel={"login"}  />
          <MenuItem onSelect={this.props.onSelect} menulabel={"register"}  />
            <MenuItem />
         
      </nav>
        )
    }
}
export default Navbar;