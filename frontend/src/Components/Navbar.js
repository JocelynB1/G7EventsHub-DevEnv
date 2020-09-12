import React from 'react';
import './Navbar.css';
import menuLogo from "./img/logo.svg"
import MenuOptions from "./MenuOptions"
class Navbar extends React.Component {

  render() {
    return (
      <nav className="menu">
        <div className="logo1">
          <img src={menuLogo} alt="" srcSet="" id="pic_logo" />
        </div>
           <MenuOptions onSelect={this.props.onSelect} status={this.props.status}/>
      </nav>
    )
  }
}
export default Navbar;