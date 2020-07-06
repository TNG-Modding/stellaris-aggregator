import React, {Component} from 'react';
import EventList from "./EventList/eventList"
import EventInfo from "./EventInfo/eventInfo"

class EventBrowser extends Component {    
    render() {
        if (this.props.selectedEvent === null)
        {
            return (
                <div className="event-handler">  
                    <EventList events={this.props.events} selectedEvent={this.props.selectedEvent} openEventFn={this.props.openEventFn}/>              
                </div>
            );
        }
        return (
            <div className="event-handler">  
                <EventList events={this.props.events} selectedEvent={this.props.selectedEvent} openEventFn={this.props.openEventFn}/>
                <EventInfo event={this.props.selectedEvent} />                
            </div>
        );
    }    
}

export default EventBrowser;