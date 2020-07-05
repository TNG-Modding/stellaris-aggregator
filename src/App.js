import React, {Component} from 'react';
// import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import './dark.css';


import ConversationPanel from "./components/conversationPanel"

class App extends Component {
  render () {
    return (
      <div className="container-fluid h-100"> 
        <ConversationPanel />
      </div>
    );
  }
}

export default App;
