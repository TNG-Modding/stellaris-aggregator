import React, {Component} from 'react';
import EventOptionItem from "./eventOptionItem"

class EventOptionList extends Component {
    render() {
        if (this.props.event === undefined || this.props.event.options === undefined) {
            console.log("Event has no options or is undefined")
            return (
                <div><p>Options</p></div>
            )
        }
        return (
            <div>
                <p>Options</p>
                <ul className="list-group">
                    {this.props.event.options.map((option, index) => 
                        <EventOptionItem key={index} option={option}/>
                    )}            
                </ul>
            </div>
        );
    }
}

export default EventOptionList;