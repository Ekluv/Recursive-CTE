import React from 'react';
import ReactDOM from 'react-dom';

import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk'; // thunk middleware for aync actions in redux(doing things redux way)
import { Router, browserHistory } from 'react-router';

import HomePage from './containers/Home';
import rootReducer from './reducers';
import routes from './routes';

import "ag-grid/dist/styles/ag-grid.css";
import "ag-grid/dist/styles/theme-fresh.css";

const createStoreWithMiddleware = applyMiddleware(thunk)(createStore);



ReactDOM.render(
  <Provider store={createStoreWithMiddleware(rootReducer)}>
    <HomePage />
  </Provider>, document.querySelector('.container-fluid'))