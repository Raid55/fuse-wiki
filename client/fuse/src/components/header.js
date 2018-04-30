import React, { Component } from 'react';


class Header extends Component {
  render() {
    return (
      <div>
        <div className="ui three item menu">
          <a className="active item">Home</a>
          <a className="item">About</a>
          <a className="item">Social</a>
        </div>
      </div>
    );
  }
}

export default Header;
