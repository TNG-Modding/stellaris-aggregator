import React, {Component} from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import FileList from "./components/FileList/fileList"
import ConversationView from "./components/ConversationView/conversationView"
import EventSelector from "./components/EventSelector/eventSelector"



class App extends Component {
  componentDidMount = () => {

  }
  render () {
    return (
      <div className="container-fluid h-100"> 
        <div className="row h-100"> 
          <div className="col-md-2">
            <FileList /> 
          </div>
          <div className="col-md-4">
            <EventSelector /> 
          </div> 
          <div className="col-md-6">
            <ConversationView />
          </div>
        </div> 
      </div>
    );
  }
}

export default App;
