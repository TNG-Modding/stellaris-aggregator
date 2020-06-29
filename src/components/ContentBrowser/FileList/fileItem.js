import React, {Component} from 'react';

class FileItem extends Component {
    render() {  
        return (
            <button key={this.props.filename} 
                    type="button" 
                    onClick={() => this.onFileClick(this.props.filename)} 
                    className="list-group-item text-left">
                {this.props.filename}
            </button>
        );
    }
    onFileClick = (filename) => {
        this.props.openFileFn(filename);
    }
}

export default FileItem;