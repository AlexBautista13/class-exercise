import React from 'react';

export default class CardComponent extends React.Component {
  state = { species: '' };
  componentDidMount() {
    fetch(this.props.species[0])
      .then(response => response.json())
      .then(json => this.setState({ species: json.name }));
  }
  render() {
    return (
      <div className="Card">
        <h3>Name: {this.props.name}</h3>
        <h4 style={{ fontStyle: 'italic', color: 'red' }}>
          The species.name value should be shown below... not the url
        </h4>
        <h4>Species: {this.state.species}</h4>
      </div>
    );
  }
}