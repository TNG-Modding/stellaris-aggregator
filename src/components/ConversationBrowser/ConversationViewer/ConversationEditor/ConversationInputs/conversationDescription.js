import React, {Component} from 'react';

class ConversationDescription extends Component {
    render() {
        return (
            <div className="input-group">
                <textarea 
                    type="text" 
                    className="form-control" 
                    placeholder="Description" 
                    rows="10" 
                    readOnly
                    defaultValue={this.props.conversation.description}/>
            </div>
        );
    }
}
export default ConversationDescription;