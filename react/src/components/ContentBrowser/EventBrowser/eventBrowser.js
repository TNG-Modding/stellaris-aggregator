import React, {Component} from 'react';
import EventList from "./eventList"
import EventInfo from "./EventInfo/eventInfo"

class EventBrowser extends Component {    

    constructor() {
        super();
        this.state = {
            selectedEvent: { name: "name", description: "description!", options: [{name:"options.a"}]}
        }
    }

    render() {
        return (
            <div className="event-handler">  
                <EventList events={this.props.events} />
                <EventInfo event={this.state.selectedEvent} />                
            </div>
        );
    }    
}

export default EventBrowser;