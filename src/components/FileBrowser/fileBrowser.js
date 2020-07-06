import React, {Component} from 'react';
import FileList from "./FileList/fileList"
import EventBrowser from "./EventBrowser/eventBrowser"

class FileBrowser extends Component {
    constructor() {
        super();
        this.state = {
            filepaths: [],
            selectedFilepath: null,
            events: [],
            selectedEvent: null
        }    
    }

    async componentDidMount() {
        const filepaths = await this.props.eventsClient.getFiles("/Volumes/Storage/stellaris-defines/events");
        await this.updateFilepaths(filepaths["filepaths"])
    }

    updateFilepaths = async (paths) => {       
        this.setState(prevState => ({
            ...prevState,
            filepaths: paths,
        }));

        if (paths.length >= 1) {
            await this.openFileName(paths[0]);
        }        
    }

    openFileName = async (filepath) => {
        const parsedFile = await this.props.eventsClient.parseEventFile(filepath);
        console.log(parsedFile["file"]["events"]);
        this.setState(prevState => ({
            ...prevState,
            events: parsedFile["file"]["events"], 
            selectedFilepath:filepath
        }));
        if (parsedFile["file"]["events"].length >= 1) {
            await this.selectAnEvent(parsedFile["file"]["events"][0]);
        } 
    }

    selectAnEvent = (event) => {
        this.setState(prevState => ({
            ...prevState,
            selectedEvent: event,
        }));
    }
    
    render() {
        return (
            <div className="row">
                <div className="col-md-6">
                    <FileList filepaths={this.state.filepaths} openFileFn={this.openFileName} selectedFilepath={this.state.selectedFilepath}/>
                </div>
                <div className="col-md-6">
                    <EventBrowser events={this.state.events} selectedEvent={this.state.selectedEvent} openEventFn={this.selectAnEvent}/>
                </div>
            </div>
        );
    }    
}

export default FileBrowser;