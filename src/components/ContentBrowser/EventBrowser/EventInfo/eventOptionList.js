import React, {Component} from 'react';

class EventOptionList extends Component {
    render() {
        return (
            <div>
                <p>Options</p>
                <ul className="list-group">
                    {this.props.event.options.map((option, index) => 
                        <button key={index} type="button" className="list-group-item text-left">{option.name}</button>
                    )}            
                </ul>
            </div>
        );
    }
}

export default EventOptionList;