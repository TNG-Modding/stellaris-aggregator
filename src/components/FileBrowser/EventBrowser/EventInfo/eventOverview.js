import React, {Component} from 'react';
import ListFields from "../listFields"

class EventOverview extends Component {
    render() {
        if (this.props.event === undefined){
            return (
                <div>
                    <p>Event</p>
                </div>
            );
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