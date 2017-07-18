import React from 'react';
import {Entity, Scene} from 'aframe-react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
// import './styles.css';
import VRScene from '../../components/VRScene';

class VRView extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor(props) {
      super(props);
  }

  getSrc() {
    try {
      return this.props.images[this.props.params.index].pano;
    } catch(e) {
      this.props.history.push('/');
    }
    
  }

  render() {
    return (
      <VRScene src={this.getSrc()} />
    );
  }
}



function mapStateToProps(state) {
  return {
    images: state.data.images,
  }
}


export default connect(mapStateToProps, null)(VRView)