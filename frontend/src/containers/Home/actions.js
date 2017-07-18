import * as C from './constants'; 
import request from '../../utils/request';


export var getEmployeeList = () => {
    return function(dispatch) {
        request(C.APIENDPOINTS.GETEMPLOYEELIST).then((response) => {
            dispatch({
                type: C.FETCH_EMPLOYEES,
                data: response
            });
        });
    };
};

export var updateParent = (parentId, employeeId) => {
    return function(dispatch) {
        request(C.APIENDPOINTS.UPDATE_PARENT + employeeId + '/', {
            parent_id:parentId
        }, 'PUT').then((response) => {
            if(!response.success) {
                window.alert(response.error);
                return;
            }
            dispatch({
                type: C.UPDATE_PARENT,
                data: response
            });
        });
    };
};
