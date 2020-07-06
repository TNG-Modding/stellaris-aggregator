import React, {Component} from 'react';
import ListFields from "../listFields"

class EventButton extends Component {
    render() {
        return (
            <button 
                onClick={() => this.props.openEventFn(this.props.event)} 
                key={this.props.index.toString()} 
                type="button" 
                className={"list-group-item text-left " + (this.props.selectedEvent === this.props.event ? "active-event-item" : "")}>
                <ListFields className="event-item-name" fields={this.props.event.ids}/>
                <span className="event-item-option-count">{this.getOptionCount()}</span>
            </button>
        );
    }
    getOptionCount = () => {
        if (this.props.event.options === undefined) {
            return "";
        }
        return "" + this.props.event.options.length + " options";
    }
}
export default EventButton;