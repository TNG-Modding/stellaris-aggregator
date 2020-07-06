import React, {Component} from 'react';
import ConversationSourceItem from "./conversationSourceItem"

class ConversationSourceList extends Component {
    render() {
        return (
        <div>
            <h4>Sources</h4>
            <ul className="list-group">
                {this.props.conversation.optionLocations.map(conversationSource => 
                    <ConversationSourceItem conversationSource={conversationSource}/>
                )}
            </ul>
        </div>
        );
    }
}
export default ConversationSourceList;