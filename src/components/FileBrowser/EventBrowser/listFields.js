import React, {Component} from 'react';

class ListFields extends Component {
    render() {
        if (this.props.fields === undefined) {
            return null;
        }
        return (
            <span>
                {this.props.fields.map((item, index) => 
                    <span key={index}>{item.toString()} </span>
                )}  
            </span>
        );
    }
}

export default ListFields;