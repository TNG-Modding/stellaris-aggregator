import React, {Component} from 'react';
import ConversationView from "./ConversationView/conversationView"
import ContentBrowser from "./ContentBrowser/contentBrowser"

class ConversationPanel extends Component {
  render () {
    return (
        <div className="row h-100"> 
          <div className="col-md-6">
            <ContentBrowser /> 
          </div> 
          <div className="col-md-6">
            <ConversationView />
          </div>
        </div> 
    );
  }
}

export default ConversationPanel;
