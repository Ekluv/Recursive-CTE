import { combineReducers } from 'redux';
import employeesReducer from './containers/Home/reducers';

const rootReducer = combineReducers({
	data: employeesReducer
});

export default rootReducer;
