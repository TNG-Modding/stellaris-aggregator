import React, {Component} from 'react';
import FileList from "./FileList/fileList"
import EventBrowser from "./EventBrowser/eventBrowser"

class FileBrowser extends Component {
    constructor() {
        super();
        this.state = {
            events: [],
            filepaths: [],
            selectedFilepath: null
        }    

    }

    updateFilepaths(paths) {
        this.setState(prevState => ({
            ...prevState,
            filepaths: paths
        }));
    }

    async componentDidMount() {
        const filepaths = await this.props.eventsClient.getFiles("/Volumes/Storage/stellaris-defines/events");
        this.updateFilepaths(filepaths["filepaths"])
    }

    openFileName = async (filepath) => {
        const parsedFile = await this.props.eventsClient.parseEventFile(filepath);
        console.log(parsedFile["file"]["events"])
        this.setState({events: parsedFile["file"]["events"], selectedFilepath:filepath})
    }
    
    render() {
        return (
            <div className="row">
                <div className="col-md-6">
                    <FileList filepaths={this.state.filepaths} openFileFn={this.openFileName} selectedFilepath={this.state.selectedFilepath}/>
                </div>
                <div className="col-md-6">
                    <EventBrowser events={this.state.events}/>
                </div>
            </div>
        );
    }    
}

export default FileBrowser;