import React, {Component} from 'react';

class ConversationEditor extends Component {
    render() {
        return (
        <div className="ConversationEditor">
            <p>Varname: {this.props.varname}</p>
            <div className="input-group">
            <span className="input-group-addon" id="basic-addon1">Name</span>
            <input type="text" className="form-control" placeholder="Conversation" aria-describedby="basic-addon1">{this.props.name}</input>
            </div>
            <div className="input-group">
            <textarea type="text" className="form-control"  placeholder="Description" aria-describedby="basic-addon1" rows="10">{this.props.description}</textarea>
            </div>
            <div className="input-group">
                <span className="input-group-addon" id="basic-addon1">Ethic</span>
                <input type="text" className="form-control" placeholder="xenophile" aria-describedby="basic-addon1">{this.props.ethic}</input>
            </div>
            <div className="input-group">
                <span className="input-group-addon" id="basic-addon1">Duration in Years</span>
                <input type="text" className="form-control" placeholder="25" aria-describedby="basic-addon1">{this.props.durationYears}</input>
            </div>
        </div>
        );
    }
}
export default ConversationEditor;