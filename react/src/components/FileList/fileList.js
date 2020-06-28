import React, {Component} from 'react';

const filenames = ["/Volumes/Storage/stellaris-defines/events/galactic_community_events.txt", "/Volumes/Storage/stellaris-defines/events/anomalies.txt"]

class FileList extends Component {
    onFileClick = (filename) => {
        console.log(filename);
    }

    render() {  
        return (
        <div>
            <p>Event Files</p>
            <ul className="list-group">
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