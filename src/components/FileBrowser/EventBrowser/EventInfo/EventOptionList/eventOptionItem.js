import React, {Component} from 'react';
import ListFields from "../../listFields"

class EventOptionItem extends Component {
    render() {
        return (
            <li key={this.props.index} type="button" className="list-group-item option-list-item text-left ">
                <ListFields className="option-list-names" fields={this.props.option.names}/>
            </li>
        );
    }
}

export default EventOptionItem;