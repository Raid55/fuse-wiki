import React, { Component } from 'react';


class Header extends Component {
  render() {
    return (
      <div>
        <div className="ui inverted massive borderless secondary pointing menu">
          <div className="item">FUSE</div>
          <div className="right menu">
            <a className="active item">Home</a>
            <a className="item">About</a>
            <a className="item">Social</a>
          </div>
        </div>
        <br />
      </div>
    );
  }
}

export default Header;
