import React, {Component} from 'react';
import ConversationViewer from "./ConversationViewer/conversationViewer"
import ConversationList from "./ConversationList/conversationList"

class ConversationBrowser extends Component {
    constructor() {
        super();
        this.state = {
            conversations: [],
            editedConversations: {},
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
        if (response["conversations"].length >= 1) {
            this.selectAConversation(response["conversations"][0]);
        }
    }

    selectAConversation = (conversation) => {
        this.setState(prevState => ({
            ...prevState,
            selectedConversation: conversation
        }));
    }

    updateAConversation = (conversationWithEdits) => {

    }

    render(){
        return (
            <div className="row">
                <div className="col-md-4 ">
                    <ConversationList conversations={this.state.conversations} selectedConversation={this.state.selectedConversation} openConversationFn={this.selectAConversation}/>
                </div>
                <div className="col-md-8">
                    <ConversationViewer conversation={this.state.selectedConversation} />
                </div>
            </div>
        );
    }
}

export default ConversationBrowser;