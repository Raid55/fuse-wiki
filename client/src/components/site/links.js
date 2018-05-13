import React, { Component } from 'react';


class Link extends Component {
  render() {
    return (
      <div className="ui centered grid">
        <div className="ui eight wide column">
          <div className="">
            { this.props.links.map(ell => <div className="ui center aligned segment" key={ell}>{ell}</div>)}
          </div>
        </div>
      </div>
    );
  }
}

export default Link;