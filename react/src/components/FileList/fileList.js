import React, {Component} from 'react';

const filenames = ["galactic_community_events.txt", "anomalies.txt"]

class FileList extends Component {
    onFileClick = (filename) => {
        console.log(filename);
    }

    render() {  
        return (
        <div className="file-list h-100">
            <p>Event Files</p>
            <ul className="list-group flex-grow-1">
                {filenames.map(filename => 
                    <button key={filename} type="button" 
                        onClick={() => this.onFileClick(filename)} className="list-group-item">
                        {filename}
                    </button>
                )}            
            </ul>
        </div>
        );
    }
}

export default FileList;