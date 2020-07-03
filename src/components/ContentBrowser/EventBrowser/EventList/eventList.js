import React, {Component} from 'react';
import EventButton from "./eventButton"

class EventList extends Component {
    render() {
        return (
            <div>
                <p>Events</p>
                <ul className="list-group">
                    {this.props.events.map((event, index) => 
                        <EventButton event={event} index={index} openEventFn={this.props.openEventFn}/>
                    )}            
                </ul>
            </div>
        );
    }
}
export default EventList;