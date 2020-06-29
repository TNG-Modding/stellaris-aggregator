import React, {Component} from 'react';
import FileItem from "./fileItem"

const filenames = ["galactic_community_events.txt", "anomalies.txt"]

class FileList extends Component {
    onFileClick = (filename) => {
        this.props.openFileFn(filename);
    }

    componentDidMount = () => {
        
    }

    render() {  
        return (
        <div className="file-list h-100">
            <p>Event Files</p>
            <ul className="list-group flex-grow-1">
                {filenames.map(filename => 
                    <FileItem filename={filename} openFileFn={this.props.openFileFn}/>
                )}            
            </ul>
        </div>
        );
    }
}

export default FileList;