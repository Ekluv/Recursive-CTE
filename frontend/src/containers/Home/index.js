import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as homeActions from './actions';
import SpreadSheet from '../../components/SpreadSheet';
import './styles.css';

class HomePage extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor(props) {
      super(props);
      this.props.getEmployeeList();
  }

  render() {
    return (
        <SpreadSheet employees={this.props.employees} onParentChange={this.props.updateParent}/>
      );
    }
  }


function mapStateToProps(state) {
  console.log(state);
  return {
    employees: state.data.employees,
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators({...homeActions}, dispatch)
}

export default connect(mapStateToProps, mapDispatchToProps)(HomePage)