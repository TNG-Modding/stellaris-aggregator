import React, {Component} from 'react';
import FileList from "./FileList/fileList"
import EventBrowser from "./EventBrowser/eventBrowser"
import EventClient from "../../clients/eventClient"

const eventClient = new EventClient();

class ContentBrowser extends Component {
    constructor() {
        super();
        this.state = {
            events: [{ name: "First event", description: "description!", options: [{name:"options.a"}]}],
            filepaths: []
        }    

    }

    updateFilepaths(paths) {
        this.setState(prevState => ({
            ...prevState,
            filepaths: paths
        }));
    }

    async componentDidMount() {
        const filepaths = await eventClient.getFiles("/Volumes/Storage/stellaris-defines/events");
        this.updateFilepaths(filepaths["filepaths"])
    }

    openFileName = async (filename) => {
        const parsedFile = await eventClient.parseEventFile(filename);
        console.log(parsedFile)
        this.setState({events: [{ name: "First event", description: "description!", options: [{name:"options.a"}]}]})
    }
    
    render() {
        return (
            <div className="row">
                <div className="col-md-6">
                    <FileList filepaths={this.state.filepaths} openFileFn={this.openFileName}/>
                </div>
                <div className="col-md-6">
                    <EventBrowser events={this.state.events}/>
                </div>
            </div>
        );
    }    
}

export default ContentBrowser;