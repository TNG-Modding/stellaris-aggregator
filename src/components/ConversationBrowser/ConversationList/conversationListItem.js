import React, {Component} from 'react';

class ConversationListItem extends Component {
    render() {
        return (
            <button 
                key={this.props.index} 
                type="button" 
                onClick={() => this.props.openConversationFn(this.props.conversation)} 
                className={"list-group-item text-left conversation-list-item " + 
                    (this.props.selectedConversation === this.props.conversation ? "active-conversation-item" : "")}>
                    {this.props.conversation.name}
            </button>
        );
    }
}
export default ConversationListItem;