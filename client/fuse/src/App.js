import React, { Component } from 'react';
import Header from './components/header';
import Fuse from './components/site';

class App extends Component {
  render() {
    return (
      <div>
        <div className="ui center aligned container">
          <Header />
          <Fuse />
          <button>owowow</button>
        </div>
      </div>
    );
  }
}

export default App;
