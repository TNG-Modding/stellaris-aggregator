import React, {Component} from 'react';
import EventList from "./eventList"
import EventInfo from "./EventInfo/eventInfo"

class EventBrowser extends Component {    

    // constructor() {
    //     super();
    //     this.state = {
    //         selectedEvent: this.props.events[0]
    //     }
    // }

    render() {
        return (
            <div className="event-handler">  
                <EventList events={this.props.events} />
                <EventInfo event={this.props.events[0]} />                
            </div>
        );
    }    
}

export default EventBrowser;