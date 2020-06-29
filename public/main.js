const {PythonShell} = require('python-shell');
const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

const path = require('path');
const url = require('url');
const isDev = require('electron-is-dev');

let mainWindow;

require('electron-reload')(__dirname);

function createWindow() {
  mainWindow = new BrowserWindow({width: 1920,
    height: 1080,});
  mainWindow.loadURL(isDev ? 'http://localhost:3000' : `file://${path.join(__dirname, '../build/index.html')}`);
  mainWindow.on('closed', () => mainWindow = null);
  mainWindow.webContents.openDevTools();
}

function startPythonServer() {
  var serverMainFilepath = path.join(__dirname, '/../backend/main.py');
  // var subpy = require('child_process').spawn('python', [serverMainFilepath]);
  PythonShell.run(serverMainFilepath,  function  (err, results)  {
    if (err) {
      console.log(err);
      return;
    }
  }); 
}

app.on('ready', function(){
  // startPythonServer();
  createWindow();  
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});