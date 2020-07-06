import React, {Component} from 'react';

class ConversationVarname extends Component {
    render() {
        return (
            <p>Varname: {this.props.conversation.varname}</p>
        );
    }
}
export default ConversationVarname;