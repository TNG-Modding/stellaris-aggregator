import React, {Component} from 'react';
import ListFields from "./listFields"

class EventList extends Component {
    render() {
        return (
            <div>
                <p>Events</p>
                <ul className="list-group">
                    {this.props.events.map((event, index) => 
                        <button key={index} type="button" className="list-group-item text-left">
                            <ListFields fields={event.ids}/>
                        </button>
                    )}            
                </ul>
            </div>
        );
    } 
}
export default EventList;