import React, {Component} from 'react';
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

const filenames = ["/Volumes/Storage/stellaris-defines/events/galactic_community_events.txt", "/Volumes/Storage/stellaris-defines/events/anomalies.txt"]
const options = [{name: "Option name", id: 1}]
const events = [{name: "Event name", id: 1}]
const conversations = [{name: "Conversation name", id: 1}]

function FileList (props) {
  return (
      <div>
          <p>Event Files</p>
          <ul className="list-group">
              {filenames.map(filename => 
                  <button key={filename} type="button" onclick="parseEventFile('{filename}')" className="list-group-item">{filename}</button>
              )}            
          </ul>
      </div>
  );
}

function EventList (props) {
  return (
      <div>
          <p>Event</p>
          <ul className="list-group">
              {events.map(event => 
                  <button key={event.Id} type="button" className="list-group-item">{event.Name}</button>
              )}            
          </ul>
      </div>
  );
}

function EventOptionList (props) {
  return (
      <div>
          <p>Options</p>
          <ul className="list-group">
              {options.map(option => 
                  <button key={option.Id} type="button" className="list-group-item">{option.Name}</button>
              )}            
          </ul>
      </div>
  );
}

function EventSelector (props) {
  return (
    <div>
        <EventList />
        <EventOverview />
        <EventOptionList />
    </div>
  );
}



function ConversationEditor (props) {
  return (
    <div className="row">
      <div className="col-xs-4">
        <ConversationList />
      </div>
      <div className="col-xs-8">
        <ConversationViewer />
      </div>
    </div>
  );
}

function ConversationList (props) {
  return (
      <div>
          <p>Conversations</p>
          <ul className="list-group">
              {conversations.map(conversation => 
                  <button key={conversation.Id} type="button" className="list-group-item">{conversation.Name}</button>
              )}            
          </ul>
      </div>
  );
}

function ConversationViewer(props) 
{
  return (
    <div>
      <p>Varname</p>
      <p>Options</p>
      <div className="list-group">
        <a href="/" className="list-group-item">
            <span>Filename</span> /
            <span>Eventname</span> /
            <span>Option</span>
        </a>
        <a href="/" className="list-group-item">
          <span>Filename</span> /
          <span>Eventname</span> /
          <span>Option</span>
        </a>
      </div>
      
      <div className="input-group">
        <span className="input-group-addon" id="basic-addon1">Name</span>
        <input type="text" className="form-control" placeholder="Conversation" aria-describedby="basic-addon1"></input>
      </div>
      <div className="input-group">
        <textarea type="text" className="form-control"  placeholder="Description" aria-describedby="basic-addon1" rows="10"></textarea>
      </div>
      <div className="row row-no-gutters">
        <div className="col-xs-6">
          <div className="input-group">
            <span className="input-group-addon" id="basic-addon1">Ethic</span>
            <input type="text" className="form-control" placeholder="xenophile" aria-describedby="basic-addon1"></input>
          </div>
        </div>
        <div className="col-xs-6">
          <div className="input-group">
            <span className="input-group-addon" id="basic-addon1">Duration in Years</span>
            <input type="text" className="form-control" placeholder="25" aria-describedby="basic-addon1"></input>
          </div>
        </div>
      </div>
      
      
      <h4>Demands</h4>
      <ul className="list-unstyled">
        <li>Demand</li>
        <li>Demand</li>
        <li>Demand</li>
      </ul>
      
      <div className="row">
        <div className="col-xs-10">
          <div className="input-group">
            <input type="text" className="form-control" placeholder="Demand"></input>
              <span className="input-group-btn">
                <button className="btn btn-default" type="button">Add</button>
              </span>
            
          </div>
        </div>
        <div className="col-xs-2">
          <button type="button" className="btn btn-default">Delete</button>
        </div>
      </div>
    </div>
  );
}

function EventOverview(props) {
  return (
    <div>
        <h3>Event</h3>
        <p>Description</p>
        <p>Options</p>
    </div>
  );
}

function App() {
  return (
    <div className="container-fluid">
      <div className="row">
        <div className="col-xs-2">
          <FileList />
        </div>
        <div className="col-xs-2">
          <EventSelector />
        </div>
        <div className="col-xs-8">
          <ConversationEditor />
        </div>
      </div>
    </div>
  );
}

export default App;
