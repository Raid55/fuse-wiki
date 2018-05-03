import React, { Component } from 'react';


class Link extends Component {
  render() {
    return (
      <div>

          { this.props.links.result[0].map(ell => <div className="ui segment" key={ell}>{ell}</div>)
          }
      </div>
    );
  }
}

export default Link;