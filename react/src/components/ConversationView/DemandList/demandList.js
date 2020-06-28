import React, {Component} from 'react';
import AddDemand from "./addDemand"
import DemandItem from "./demandItem"

class DemandsList extends Component {

    constructor () {
        super();
        this.state = {
            demands: []
        }
    }

    render() {
        return (
        <div className="demands-list">
            <h4>Demands</h4>
            <ul className="list-group">
            {this.state.demands.map((demand, index) => 
                <DemandItem demand={demand} key={demand} index={index} removeDemandFn={this.RemoveDemand}/>
            )}
            </ul>
            
            <AddDemand addDemandFn={this.AddDemand}/>
        </div>
        );
    }

    AddDemand = async (demand) => {
        var arrayLength = this.state.demands.length;
        for (var i = 0; i < arrayLength; i++) {
            if (this.state.demands[i] === demand) {
                return 1;
            }
        }
        await this.setState({demands: [...this.state.demands, demand]});
        return 0;
    }

    RemoveDemand = async (demand) => {
        await this.setState({demands: this.state.demands.filter(d => d !== demand )});
    }
}
export default DemandsList;