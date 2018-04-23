import React, { Component } from 'react';
import Form from './form';
import Links from './links';

export default class extends Component {
  render() {
    return (
      <div>
          <Form /> {/*pass props to get form change*/}
          <Links />{/*pass to update link state*/}
      </div>
    );
  }
}