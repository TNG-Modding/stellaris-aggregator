import React, {Component} from 'react';

class EventOverview extends Component {
    render() {
        return (
            <div>
                <p>Event</p>
                <p>Name: {this.props.event.name}</p>
                <p>Desc: {this.props.event.description}</p>
            </div>
        );
    }
}
export default EventOverview;