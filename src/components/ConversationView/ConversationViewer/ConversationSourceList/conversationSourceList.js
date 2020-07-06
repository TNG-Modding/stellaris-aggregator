import React, {Component} from 'react';
import ConversationSourceItem from "./conversationSourceItem"

class ConversationSourceList extends Component {
    render() {
        return (
        <div>
            <p>Conversation Sources</p>
            <ul className="list-group">
            {this.props.conversationSources.map(conversationSource => 
                <ConversationSourceItem/>
            )}
            </ul>
        </div>
        );
    }
}
export default ConversationSourceList;