import React from 'react';
import MenuOptions from './MenuOptions'
import navLogo from "./navLogo.png";
import "./index.css";

class Navbar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {

    }
  }
  onSelect = () => {
    this.props.onSelect({ requestedComponent: this.props.menulabel })
  }
  componentDidUpdate(){
    window.localStorage.setItem("requestedComponent", this.props.requestedComponent)
    setTimeout(() => this.props.setMessage(""), 5000)
  }
  render() {

    return (
      <>
        <div className="landingNav" >
          <nav className="menu">
            <div className="logoDiv">
              <img src={navLogo} className="navLogo" alt="logo" />
            </div>
            <div className="menuDiv">
              <ul className="menuList">
                <MenuOptions onSelect={this.props.onSelect} status={this.props.status} />
              </ul>
            </div>
          </nav>
        </div>
        <div id="messages" >
        {this.props.message}
        </div>
      </>
    )


  }

}
export default Navbar;