import React, { Component } from 'react';


class Link extends Component {
  render() {
    return (
      <div className="ui centered grid">
        <div className="ui eight wide column">
          <div className="">
            <div className="ui center aligned segment"><h1>Wow</h1></div>
            <img className="ui centered tiny image" src={ require('../../assets/link.png')}/>
            <div className="ui center aligned segment"><h1>wowowoow</h1></div>
            <img className="ui centered tiny image" src={ require('../../assets/link.png')}/>
            <div className="ui center aligned segment"><h1>yikes</h1></div>
            <img className="ui centered tiny image" src={ require('../../assets/link.png')}/>
            <div className="ui center aligned segment"><h1>boohoo</h1></div>
            {/* { this.props.links.result[0].map(ell => <div className="ui center aligned segment" key={ell}>{ell}</div>)} */}
          </div>
        </div>
      </div>
    );
  }
}

export default Link;