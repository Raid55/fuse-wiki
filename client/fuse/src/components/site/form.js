import React, { Component } from 'react';


class Form extends Component {
  render() {
    
    return (
      <div>
        <h1 className="ui header">Input two Wikipedia pages and press fuse</h1>
        <form className="ui form">
          <div className="two fields">
            <div className="field">
              <label>Page 1</label>
              <input type="text" name="page1" placeholder="Page 1"/>
            </div>
            <div className="field">
              <label>Page 2</label>
              <input type="text" name="page2" placeholder="Page 2"/>
            </div>
          </div>
        </form>
        <button className="ui orange button" type="submit">Fuse</button>
      </div>
    );
  }
}

export default Form;