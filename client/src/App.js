import React, { Component } from 'react';
import Header from './components/header';
import Fuse from './components/site';

class App extends Component {
  render() {
    return (
      <div>
        <Header />
        <div className="ui center aligned container">
          <Fuse />
        </div>
      </div>
    );
  }
}

export default App;
