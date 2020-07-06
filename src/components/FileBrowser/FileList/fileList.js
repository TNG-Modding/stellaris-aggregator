import React, {Component} from 'react';
import FileItem from "./fileItem"
import ListGroup from 'react-bootstrap/ListGroup';

class FileList extends Component {
    render() {  
        return (
        <div className="file-list h-100">
            <p>Event Files</p>
            <ListGroup className="flex-grow-1" variant="flush">
                {this.props.filepaths.map(filepath => 
                    <FileItem 
                        key={filepath} 
                        filepath={filepath} 
                        isSelected={this.props.selectedFilepath === filepath ? true : false} 
                        openFileFn={this.props.openFileFn}/>
                )}
            </ListGroup>
        </div>
        );
    }
}

export default FileList;