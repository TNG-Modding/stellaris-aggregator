import React, {Component} from 'react';

class DemandItem extends Component {

    render() {
        return (
            <li key={this.props.demand} className="list-group-item demand">
                <span className="demand-name">{this.props.demand}</span><span className="demand-delete" onClick={this.onRemove}>Delete</span>
            </li>
        );
    }
    onRemove = async () => {
        await this.props.removeDemandFn(this.props.demand)
    }
}
export default DemandItem;