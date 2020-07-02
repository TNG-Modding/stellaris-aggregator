import React, {Component} from 'react';
import ListFields from "../listFields"

class EventOverview extends Component {
    render() {
        if (this.props.event === undefined){
            return null;
        }
        return (
            <div>
                <p>Event</p>
                <p>Name: <ListFields fields={this.props.event.ids}/></p>
                <p>Desc: <ListFields fields={this.props.event.descriptions}/></p>
            </div>
        );
    }
}
export default EventOverview;