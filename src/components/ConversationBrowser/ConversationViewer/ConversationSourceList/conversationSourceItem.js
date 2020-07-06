import React, {Component} from 'react';

class ConversationSourceItem extends Component {
    render() {
        return (
            <button 
                key={this.props.conversationSource.filename + this.props.conversationSource.eventId + this.props.conversationSource.optionId}
                type="button" 
                className="list-group-item text-left">
                <span>{this.props.conversationSource.filename}</span> /
                <span>{this.props.conversationSource.eventId}</span> /
                <span>{this.props.conversationSource.optionId}</span>
            </button>
        );
    }
}
export default ConversationSourceItem;