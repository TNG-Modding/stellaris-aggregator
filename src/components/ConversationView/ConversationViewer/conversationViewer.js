import React, {Component} from 'react';

import DemandList from "./DemandList/demandList"
import ConversationEditor from "./conversationEditor"
import ConversationSourceList from "./ConversationSourceList/conversationSourceList"

function ConversationViewer(props) 
{
return (
    <div>
    <ConversationSourceList />
    <ConversationEditor />
    <DemandList/>
    </div>
);
}

export default ConversationViewer;