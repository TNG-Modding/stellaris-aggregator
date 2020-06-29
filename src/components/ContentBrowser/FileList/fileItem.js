import React, {Component} from 'react';

class FileItem extends Component {
    render() {  
        return (
            <button key={this.props.filepath} 
                    type="button" 
                    onClick={() => this.onFileClick(this.props.filepath)} 
                    className="list-group-item text-left file-item">
                {this.filterFilename(this.props.filepath)}
            </button>
        );
    }
    filterFilename = (filepath) => {
        return filepath.replace(/^.*[\\\/]/, '');
    }
    onFileClick = (filepath) => {
        this.props.openFileFn(filepath);
    }
}

export default FileItem;