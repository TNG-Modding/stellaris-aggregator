import React, {Component} from 'react';
import FileList from "./FileList/fileList"
import EventBrowser from "./EventBrowser/eventBrowser"
import parseEventFile from "../../linkers/eventParser"

class ContentBrowser extends Component {
    constructor() {
        super();
        this.state = {
            events: [{ name: "First event", description: "description!", options: [{name:"options.a"}]}]
        }
    }

    openFileName = (filename) => {
        console.log(filename);
        const parsedFile = parseEventFile(filename)
        console.log(parsedFile);
        this.setState({events: [{ name: "First event", description: "description!", options: [{name:"options.a"}]}]})
    }
    
    render() {
        return (
            <div className="row">
                <div className="col-md-6">
                    <FileList openFileFn={this.openFileName}/>
                </div>
                <div className="col-md-6">
                    <EventBrowser events={this.state.events}/>
                </div>
            </div>
        );
    }    
}

export default ContentBrowser;