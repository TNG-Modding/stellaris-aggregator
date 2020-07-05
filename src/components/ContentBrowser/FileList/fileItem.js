import React, {Component} from 'react';
import ListGroup from 'react-bootstrap/ListGroup';

class FileItem extends Component {
    render() {  
        return (
            <ListGroup.Item key={this.props.filepath} 
                    type="button" 
                    onClick={() => this.props.openFileFn(this.props.filepath)} 
                    className={"list-group-item text-left file-item " + (this.props.isSelected === true ? "active-file-item" : "")}>
                {this.filterFilename(this.props.filepath)}
                {this.props.isSelected}
            </ListGroup.Item>
        );
    }
    filterFilename = (filepath) => {
        return filepath.replace(/^.*[\\\/]/, '');
    }
}

export default FileItem;