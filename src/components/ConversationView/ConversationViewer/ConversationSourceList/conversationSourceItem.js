import React, {Component} from 'react';

class ConversationSourceItem extends Component {
    render() {
        return (
            <button key={this.props.filename + this.props.eventId + this.props.optionId}type="button" className="list-group-item text-left">
                <span>{this.props.filename}</span> /
                <span>{this.props.eventId}</span> /
                <span>{this.props.optionId}</span>
            </button>
        );
    }
}
export default ConversationSourceItem;