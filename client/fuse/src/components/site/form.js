import React, { Component } from 'react';


class Form extends Component {
  render() {

    return (
      <div>
        <h1 className="ui header">Input two Wikipedia pages and press fuse</h1>
        <form className="ui form" onSubmit={this.props.getLinks}>
          <div className="two fields">
            <div className="field">
              <label>Page 1</label>
              <input onChange={this.props.sourceChange} value={this.props.sourceVal} type="text" name="page1" placeholder="Page 1"/>
            </div>
            <div className="field">
              <label>Page 2</label>
              <input onChange={this.props.targetChange} value={this.props.targetVal} type="text" name="page2" placeholder="Page 2"/>
            </div>
          </div>
          <button className={ this.props.isLoading  ? "ui loading orange button" : "ui orange button" } type="text">Fuse</button>
        </form>
      </div>
    );
  }
}

export default Form;