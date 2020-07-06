import React, {Component} from 'react';
import ConversationView from "./ConversationView/conversationView"
import ContentBrowser from "./ContentBrowser/contentBrowser"

import EventClient from "../clients/eventClient"
const eventClient = new EventClient();

class ConversationPanel extends Component {
  render () {
    return (
        <div className="row h-100"> 
          <div className="col-md-6">
            <ContentBrowser eventsClient={eventClient}/> 
          </div> 
          <div className="col-md-6">
            <ConversationView eventsClient={eventClient}/>
          </div>
        </div> 
    );
  }
}

export default ConversationPanel;
