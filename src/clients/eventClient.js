const request = require('request');
const mainAddr = 'http://localhost:5000';

class EventClient {
  
  parseEventFile (filepath) {
    var options = {
      method: 'post',
      body: {filepath:filepath},
      json: true,
      url: mainAddr + "/parse"
    };
    return new Promise(function (resolve, reject) {
      request(options, (err, res, body) => {
          if (err) { 
            reject(err);  
          }     
          resolve(body);
      });
    });
  }

  getFiles (filepath) {
    var options = {
      method: 'post',
      body: {directorypath:filepath},
      json: true,
      url: mainAddr + "/files"
    };
    return new Promise(function (resolve, reject) {
      request(options, (err, res, body) => {
          if (err) { 
            reject(err);  
          }          
          resolve(body);    
      });
    });
  }
  getConversations(directorypath) {
    var options = {
      method: 'post',
      body: {directorypath:directorypath},
      json: true,
      url: mainAddr + "/conversations"
    };
    return new Promise(function (resolve, reject) {
      request(options, (err, res, body) => {
          if (err) { 
            reject(err);  
          }          
          resolve(body);    
      });
    });
  }
}

export default EventClient;  