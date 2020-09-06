import React from 'react';
import './Navbar.css';
import menuLogo from "./img/logo.svg"


class Navbar extends React.Component{

   render(){
        return(
            <nav className="menu">
            <div className="logo1">
                <img src={menuLogo} alt="" srcSet="" id="pic_logo" />
            </div>
             <a href="/">Home</a>
            <a href="/about">Menu Item 1</a>
            <a href="/blog">Menu Item 2</a>
            <a href="/contact">Menu Item 3</a>
         
      </nav>
        )
    }
}
export default Navbar;