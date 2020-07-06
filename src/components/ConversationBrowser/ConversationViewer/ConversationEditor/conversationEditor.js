import React, {Component} from 'react';
import ConversationVarname from "./ConversationInputs/conversationVarname"
import ConversationName from "./ConversationInputs/conversationName"
import ConversationDescription from "./ConversationInputs/conversationDescription"
import ConversationEthic from "./ConversationInputs/conversationEthic"
import ConversationDuration from "./ConversationInputs/conversationDuration"

class ConversationEditor extends Component {
    render() {
        return (
            <div className="ConversationEditor">
                <ConversationVarname conversation={this.props.conversation}/>
                <ConversationName conversation={this.props.conversation}/>
                <ConversationDescription conversation={this.props.conversation}/>
                <ConversationEthic conversation={this.props.conversation}/>
                <ConversationDuration conversation={this.props.conversation}/>
            </div>
        );
    }
}
export default ConversationEditor;