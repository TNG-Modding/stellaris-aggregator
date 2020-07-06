import React, {Component} from 'react';

class ConversationDuration extends Component {
    render() {
        return (
            <div className="input-group">
                <span className="input-group-addon" id="basic-addon1">Duration in Years</span>
                <input type="text" className="form-control" placeholder="25" aria-describedby="basic-addon1" value={this.props.conversation.durationYears}></input>
            </div>
        );
    }
}
export default ConversationDuration;