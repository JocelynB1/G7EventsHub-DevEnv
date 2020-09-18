import React from 'react';
import './Navbar.css';
import menuLogo from "./img/logo.svg"
import { Link } from 'react-router-dom';

class Navbar extends React.Component {

  render() {
    if (this.props.token === "") {

      return (
        <nav className="menu">
          <ul className="nav-links">
            <Link to="/register">
              <li>register</li>
            </Link>
            <Link to="/login">
              <li>login</li>
            </Link>
          </ul>
        </nav>
      )


    } else {
      return (
        <nav className="menu">
          <div className="logo1">
            <img src={menuLogo} alt="" srcSet="" id="pic_logo" />
          </div>
          <ul className="nav-links">
            <Link to="/bookAnEvent">
              <li>book an event</li>
            </Link>
           
            <Link to="/logout">
              <li>logout</li>
            </Link>
          </ul>
        </nav>
        //   <nav className="menu">
        //     <div className="logo1">
        //       <img src={menuLogo} alt="" srcSet="" id="pic_logo" />
        //     </div>
        //        <MenuOptions onSelect={this.props.onSelect} status={this.props.status}/>
        //   </nav>
      )
    }
  }
}
export default Navbar;