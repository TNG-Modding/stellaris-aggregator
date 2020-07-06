import React, {Component} from 'react';

class ConversationListItem extends Component {
    render() {
        return (
            <button key={this.props.index} type="button" className="list-group-item text-left">{this.props.conversation.name}</button>
        );
    }
}
export default ConversationListItem;