import React, {Component} from 'react';
import FileItem from "./fileItem"

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
                {this.props.filepaths.map(filepath => 
                    <FileItem filepath={filepath} openFileFn={this.props.openFileFn}/>
                )}            
            </ul>
        </div>
        );
    }
}

export default FileList;