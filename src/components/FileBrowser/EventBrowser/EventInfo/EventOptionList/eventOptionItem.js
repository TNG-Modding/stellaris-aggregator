import React, {Component} from 'react';
import ListFields from "../../listFields"

class EventOptionItem extends Component {
    render() {
        return (
            <li key={this.props.index} type="button" className="option-list-item text-left ">
                <ListFields className="option-list-names" fields={this.props.option.names}/>
                <span className="option-list-create">X</span>
                <span className="option-list-create">Open</span>
            </li>
        );
    }
}

export default EventOptionItem;