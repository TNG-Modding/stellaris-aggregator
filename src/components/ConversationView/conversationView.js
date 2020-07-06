import React, {Component} from 'react';
import ConversationViewer from "./ConversationViewer/conversationViewer"
import ConversationList from "./ConversationList/conversationList"

class ConversationView extends Component {
    constructor() {
        super();
        this.state = {
            conversations: [],
            selectedConversation: null
        }    

    }
    updateConversations(conversations) {
        this.setState(prevState => ({
            ...prevState,
            conversations: conversations
        }));
    }

    async componentDidMount() {
        const response = await this.props.eventsClient.getConversations("/Users/oliverbarnum/galactic-conversation/conversations/");
        // console.log(response);
        this.updateConversations(response["conversations"])
    }

    render(){
        return (
            <div className="row">
                <div className="col-md-4 ">
                    <ConversationList conversations={this.state.conversations}/>
                </div>
                <div className="col-md-8">
                    {/* <ConversationViewer /> */}
                </div>
            </div>
        );
    }
}

export default ConversationView;