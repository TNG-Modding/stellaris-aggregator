from __future__ import print_function
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from lib import *
from pprint import pprint

app = Flask(__name__)
CORS(app)

@app.route("/parse", methods=['POST'])
def parse():
    """Parse a file"""
    pprint(request.json["filepath"])
    directorypath = request.json["filepath"]

    filename = os.path.splitext(os.path.basename(directorypath))[0]
    jsonOutputFilepath = os.path.dirname(directorypath) + "/" + filename + ".json"
    if os.path.exists(jsonOutputFilepath):
        with open(jsonOutputFilepath, 'r') as jsonOutputFile:
            parsedFile = jsonOutputFile.read()
            return parsedFile
    else:
        parsedFile = LoadStellarisFile(directorypath)
        with open(jsonOutputFilepath, 'w') as outputFile:
            json.dump(parsedContents, outputFile, indent=2) 
        return jsonify(parsedFile)    

@app.route("/files", methods=['POST'])
def files():
    """Print the event filenames."""
    pprint(request.json["directorypath"])
    directorypath = request.json["directorypath"]
    filepaths = GetFilenamesInFolder(directorypath)
    return jsonify({"filepaths":filepaths})

@app.route("/parse-all")
def parseAll():
    """Print the event filenames."""
    # pprint(request.json["directorypath"])
    # directorypath = request.json["directorypath"]
    directorypath = "/Volumes/Storage/stellaris-defines/events"
    filepaths = GetFilenamesInFolder(directorypath)
    for filepath in filepaths:
        filename = os.path.splitext(os.path.basename(filepath))[0]
        outputFilepath = os.path.dirname(filepath) + "/" + filename + ".json"
        if os.path.exists(outputFilepath):
            print("Already parsed %s" % filename)
        else:
            print("Parsing %s " % filename)
            parsedContents = LoadStellarisFile(filepath)
            print("\tWriting contents to %s" % outputFilepath)  
            with open(outputFilepath, 'w') as outputFile:
                json.dump(parsedContents, outputFile, indent=2)      
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route("/conversations", methods=['POST'])
def conversations():
    directorypath = request.json["directorypath"]
    conversations = {}
    conversations["conversations"] = ReadConversationsInFolder(directorypath)
    return jsonify(conversations)

@app.route("/localization/<path:localizationpath>", methods=['POST'])
def localization(localizationpath):
    """Load the localization contents."""
    localizations = GetLocalizationContentsInFolder(localizationpath)
    print(localizations)
    return localizations

if __name__ == "__main__":
    print('Server starting 127.0.0.1:5000')
    app.run(host='127.0.0.1', port=5000, debug=True)