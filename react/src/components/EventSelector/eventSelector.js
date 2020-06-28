import React, {Component} from 'react';

const options = [{name: "Option name", id: 1}]
const events = [{name: "Event name", id: 1}]

function EventList (props) {
return (
    <div>
        <p>Event</p>
        <ul className="list-group">
            {events.map(event => 
                <button key={event.Id} type="button" className="list-group-item">{event.Name}</button>
            )}            
        </ul>
    </div>
);
}

function EventOptionList (props) {
return (
    <div>
        <p>Options</p>
        <ul className="list-group">
            {options.map(option => 
                <button key={option.Id} type="button" className="list-group-item">{option.Name}</button>
            )}            
        </ul>
    </div>
);
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