import React, {Component} from 'react';

import DemandList from "./DemandList/demandList"
import ConversationEditor from "./ConversationEditor/conversationEditor"
import ConversationSourceList from "./ConversationSourceList/conversationSourceList"

class ConversationViewer extends Component {
    render(){
        if (this.props.conversation === null){
            return <p>Load a conversation.</p>
        }
        return (
            <div>
            <ConversationSourceList conversation={this.props.conversation}/>
            <ConversationEditor conversation={this.props.conversation}/>
            <DemandList conversation={this.props.conversation}/>
            </div>
        );
    }    
}

export default ConversationViewer;