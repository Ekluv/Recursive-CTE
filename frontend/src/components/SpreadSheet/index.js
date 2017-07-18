import React, {Component} from "react";
import {AgGridReact} from "ag-grid-react";

export default class extends Component {
    constructor(props) {
        super(props);
        console.log(props);

        this.state = {
            columnDefs: this.createColumnDefs(),
            rowData: this.createRowData()
        };
    }

    onGridReady(params) {
        console.log('onGridReady')
        this.gridApi = params.api;
        this.columnApi = params.columnApi;
        this.gridApi.sizeColumnsToFit();
    }

    createRowData() {
        return this.props.employees;
    }



    componentWillReceiveProps(props){
        console.log('componentWillReciveProps',props);
        this.setState((prevState, props) => {
          return {rowData: props.employees};
        });
        
    }

    createColumnDefs() {
        return [
            {headerName: "ID", field: "id"},
            {headerName: "Name", field: "name"},
            {headerName: "Joining Date", field: "joining_date"},
            {headerName: "Age", field: "age"},
            {headerName: "Birthdate", field: "birthdate"},
            {headerName: "Address", field: "address"},
            {headerName: "Designation", field: "designation"},
            {headerName: "parent", field: "parent", editable: true, 
                onCellValueChanged: (event) => {
                console.log(event);
                let newValue = parseInt(event.newValue);
                if(isNaN(newValue)){
                    window.alert('Please enter integer value');
                    return;
                }
                let employeeId = event.data.id;
                console.log(employeeId, newValue);
                this.props.onParentChange(newValue, employeeId);
            }
        }
        ];
    }

    cellValueChanged() {

        console.log('cellValueChanged');
    }

    onRowEditingStopped(event) {
        console.log(event);
    }

    render() {
        let containerStyle = {
            height: 400,
            width: 800,
            margin: '0 auto'
        };

        return (
            <div style={containerStyle} className="ag-fresh">
                <h1>ag-Grid React</h1>
                <AgGridReact
                    // properties
                    columnDefs={this.state.columnDefs}
                    rowData={this.state.rowData}

                    // events
                    rowClicked={() => console.log('rowClicked')}
                    cellClicked={() => console.log('cellClicked')}
                    onRowEditingStopped={() => this.onRowEditingStopped()}
                    cellValueChanged={this.cellValueChanged.bind(this)}
                    onGridReady={this.onGridReady.bind(this)}>
                </AgGridReact>
                <p> Please Press enter while changing parent to update Data</p>
            </div>
        )
    }
};