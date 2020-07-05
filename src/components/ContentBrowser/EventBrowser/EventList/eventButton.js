import React, {Component} from 'react';
import ListFields from "../listFields"

class EventButton extends Component {
    render() {
        return (
            <button 
                onClick={() => this.selectAnEvent(this.props.event)} 
                key={this.props.index.toString()} 
                type="button" 
                className={"list-group-item text-left " + (this.props.selectedEvent === this.props.event ? "active-event-item" : "")}>
                <ListFields fields={this.props.event.ids}/>
            </button>
        );
    } 

    selectAnEvent = (event) => {
        this.props.openEventFn(event)
    }
}
export default EventButton;