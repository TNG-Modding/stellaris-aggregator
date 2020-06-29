import React, {Component} from 'react';

class EventList extends Component {
    render() {
        return (
            <div>
                <p>Events</p>
                <ul className="list-group">
                    {this.props.events.map((event, index) => 
                        <button key={index} type="button" className="list-group-item text-left">{event.name}</button>
                    )}            
                </ul>
            </div>
        );
    } 
}
export default EventList;