import React, {Component} from 'react';
import ListFields from "../listFields"

class EventOptionItem extends Component {
    render() {
        return (
            <li key={this.props.index} type="button" className="option-list-item list-group-item text-left ">
                <ListFields className="option-list-names" fields={this.props.option.names}/>
                <span className="option-list-create">Create</span>
            </li>
        );
    }
}

export default EventOptionItem;