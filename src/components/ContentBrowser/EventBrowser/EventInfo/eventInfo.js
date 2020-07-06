import React, {Component} from 'react';
import EventOverview from './eventOverview';
import EventOptionList from './EventOptionList/eventOptionList';

class EventInfo extends Component {
    render() {
        return (
            <div>
                <EventOverview event={this.props.event}/>
                <EventOptionList event={this.props.event}/>
            </div>
            
        );
    }
    
}
export default EventInfo;