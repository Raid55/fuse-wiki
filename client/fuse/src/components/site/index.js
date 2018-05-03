import React, { Component } from 'react';
import Form from './form';
import Links from './links';

export default class extends Component {
  state = {
    isLoading: false,
    links: null,
    error: false,
    sourceVal: "",
    targetVal: ""
  }

  getLinks = async (e) => {
    e.preventDefault();

    fetch('http://206.189.73.204:5000/v1/generate_link',
    {
      method: 'post',
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({raw_source_title: this.state.sourceVal, raw_target_title: this.state.targetVal})
    })
      .then( res => res.json())
      .then( res => {
        console.log(res)
        this.setState({links: res, isLoading: false});
      })
      .catch( err => {
        this.setState({error: true, isLoading: false});
        console.log(err);
      })

    this.setState({isLoading: true});
  }

  sourceChange = async (e) => {
    e.preventDefault();
    this.setState({sourceVal: e.target.value})
  }

  targetChange = async (e) => {
    e.preventDefault();
    this.setState({targetVal: e.target.value})
  }

  render() {
    return (
      <div className="ui vertical masthead center aligned segment">
          <Form
            getLinks={this.getLinks}
            isLoading={this.state.isLoading}
            sourceVal={this.state.sourceVal}
            targetVal={this.state.targetVal}
            sourceChange={this.sourceChange}
            targetChange={this.targetChange}
          />
          {this.state.links ? <Links links={this.state.links} /> : <h1>Please enter values</h1>}
      </div>
    );
  }
}