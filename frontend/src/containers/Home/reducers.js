import * as C from './constants'; 
import Immutable from 'immutable';

const INITIAL_STATE = {employees: []};

var employeesReducer = (state=INITIAL_STATE, action) => {
    switch (action.type) {
        case C.FETCH_EMPLOYEES:
            return {...state, employees: action.data}; // ES6 way to clone obj
    };

    return state
};

export default employeesReducer;