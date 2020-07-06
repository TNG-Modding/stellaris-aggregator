import React, {Component} from 'react';
import ConversationBrowser from "./ConversationBrowser/conversationBrowser"
import FileBrowser from "./FileBrowser/fileBrowser"

import EventClient from "../clients/eventClient"
const eventClient = new EventClient();

class ConversationPanel extends Component {
  render () {
    return (
        <div className="row h-100"> 
          <div className="col-md-6">
            <FileBrowser eventsClient={eventClient}/> 
          </div> 
          <div className="col-md-6">
            <ConversationBrowser eventsClient={eventClient}/>
          </div>
        </div> 
    );
  }
}

export default ConversationPanel;
