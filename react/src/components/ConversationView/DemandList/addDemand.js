import React, {Component} from 'react';

class AddDemand extends Component {

    constructor() {
        super();
        this.state = {
            demand: ''
        }
    }

    render() {
        return (
            <div className="add-demand">
                <form>           
                    <div className="input-group">
                        <input id="demand-input" onChange={(e) => this.onChangeDemandName(e)}  type="text" className="form-control" placeholder="Demand"></input>
                        <span className="input-group-btn">
                            <button onClick={(e) => this.onSubmitDemand(e)} type="submit" className="btn btn-default">Add</button>
                        </span>
                    </div>
                </form>  
            </div>
        );

    }
    onChangeDemandName = (e) => {
        this.setState({demand: e.target.value});
    }   
    onSubmitDemand = async (e) => {
        e.preventDefault();
        if (this.state.demand === ""){
            return;
        }
        const result = await this.props.addDemandFn(this.state.demand)
        if (result !== 0) {
            return;
        }
        document.getElementById("demand-input").value = ""
        this.setState({demand: ""});
    }
}
export default AddDemand;