import React, { Component } from 'react';


class Form extends Component {
  render() {

    return (
      <div className="ui centered grid">
        <div className="eight wide column">
          <div className="ui massive fluid input"><input onChange={this.props.sourceChange} value={this.props.sourceVal} type="text" name="page1" placeholder="Page 1"/></div>
        </div>
        <div className="eight wide column">
          <div className="ui massive fluid input"><input onChange={this.props.targetChange} value={this.props.targetVal} type="text" name="page2" placeholder="Page 2"/></div>
        </div>
        <div className="two wide column">
          <button className={ this.props.isLoading  ? "ui loading orange massive button" : "ui orange massive button" } type="text" onClick={this.props.getLinks}>Fuse</button>
        </div>
      </div>
    );
  }
}

export default Form;