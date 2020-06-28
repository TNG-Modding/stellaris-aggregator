import React, {Component} from 'react';

const options = [{name: "Option name", id: 1}];

class EventList extends Component {
    constructor () {
        super();
        this.state = {
            events: [{name: "Event name"}]
        }
    }
    render() {
        return (
            <div>
                <p>Events</p>
                <ul className="list-group">
                    {this.state.events.map((event, index) => 
                        <button key={index} type="button" className="list-group-item">{event.name}</button>
                    )}            
                </ul>
            </div>
        );
    }
}

class EventOptionList extends Component {
    constructor () {
        super();
        this.state = {
            events: [{name: "Option name"}]
        }
    }
    render() {
        return (
            <div>
                <p>Options</p>
                <ul className="list-group">
                    {options.map((option, index) => 
                        <button key={index} type="button" className="list-group-item">{option.name}</button>
                    )}            
                </ul>
            </div>
        );
    }
    
}

function EventSelector (props) {
return (
    <div>
        <EventList />
        <EventOverview />
        <EventOptionList />
    </div>
);
}

function EventOverview(props) {
return (
    <div>
        <h3>Event</h3>
        <p>Description</p>
    </div>
);
}
export default EventSelector;