import React, {Component} from 'react';
import ConversationListItem from "./conversationListItem"

class ConversationList extends Component {
    render() {
        return (
            <div>
                <p>Conversations</p>
                <ul className="list-group">
                    {this.props.conversations.map((conversation, index) => 
                        <ConversationListItem 
                            key={index} 
                            index={index}
                            openConversationFn={this.props.openConversationFn} 
                            conversation={conversation}
                            selectedConversation={this.props.selectedConversation} />
                    )}            
                </ul>
            </div>
        );
    }
}
export default ConversationList;