import React, { Component } from 'react';
import Form from './form';
import Links from './links';

export default class extends Component {
  state = {
    isLoading: false,
    links: [],
    error: false,
    sourceVal: "",
    targetVal: ""
  }

  getLinks = async (e) => {
    e.preventDefault();

    fetch('api.fuse.wiki/v1/generate_link')
      .then( res => {
        this.setState({links: res.json(), isLoading: false});
      });
      .catch( err => {
        this.setState({error: true, isLoading: false});
      })

    this.setState({isLoading: true});
  }

  render() {
    return (
      <div>
          <Form /> {/*pass props to get form change*/}
          <Links />{/*pass to update link state*/}
      </div>
    );
  }
}