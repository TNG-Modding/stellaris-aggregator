import React, {Component} from 'react';

class ConversationName extends Component {
    render() {
        return (
            <div className="input-group">
                <span className="input-group-addon" id="basic-addon1">Name</span>
                <input type="text" className="form-control" placeholder="Conversation" aria-describedby="basic-addon1" value={this.props.conversation.name}></input>
            </div>
        );
    }
}
export default ConversationName;