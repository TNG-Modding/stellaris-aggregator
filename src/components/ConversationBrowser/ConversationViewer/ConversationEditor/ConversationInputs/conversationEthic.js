import React, {Component} from 'react';

class ConversationEthic extends Component {
    render() {
        return (
            <div className="input-group">
                <span className="input-group-addon" id="basic-addon1">Ethic</span>
                <input type="text" className="form-control" placeholder="xenophile" aria-describedby="basic-addon1" value={this.props.conversation.ethic}></input>
            </div>
        );
    }
}
export default ConversationEthic;